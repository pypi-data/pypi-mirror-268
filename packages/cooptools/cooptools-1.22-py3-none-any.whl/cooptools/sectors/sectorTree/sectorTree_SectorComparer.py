from cooptools.sectors import RectGrid
from cooptools.geometry_utils import rect_utils as rect
from cooptools.geometry_utils import vector_utils as vec
from typing import Dict, Any, Tuple, List, Callable
import cooptools.sectors.sect_utils as sec_u
from cooptools.coopEnum import CardinalPosition
import logging
import matplotlib.patches as patches
from cooptools.colors import Color
from cooptools.plotting import plot_series

logger = logging.getLogger(__name__)

class SectorTree:
    def __init__(self,
                 area_rect: rect.Rect,
                 capacity: int,
                 shape: Tuple[int, int],
                 parent=None, lvl:int = None,
                 max_lvls: int = None):
        self.parent = parent
        self.children: Dict[Tuple[int, int], SectorTree] = {}
        self.capacity = capacity
        self.grid = RectGrid(shape[0], shape[1])
        self._area = area_rect
        self._client_mapping = {}
        self._last_mapped_pos = {}
        self.lvl = lvl if lvl else 0
        self.max_lvls = max_lvls

    def __str__(self):
        return f"{self.grid}, \n{self.children}"

    def _add_child_layer(self, grid_pos: Tuple[int, int], sector_comparer: rect.RectComparer):
        child_rect = sec_u.sector_rect(
            sector_dims=sec_u.sector_dims(area_dims=(self._area[2], self._area[3]),
                                          sector_def=self.grid.Shape
                                          ),
            sector=grid_pos,
            area_origin=(self._area[0], self._area[1])
        )

        # add a new SectorTree as a child to the grid pos
        self.children[grid_pos] = SectorTree(area_rect=child_rect,
                                             capacity=self.capacity,
                                             shape=self.grid.Shape,
                                             parent=self,
                                             lvl=self.lvl+1,
                                             max_lvls=self.max_lvls)

        # update clients in child at grid pos. This should happen whenever you add a child. it should iterate the
        # clients at the grid pos and add them to the child layer appropriately
        clients = self._client_mapping.get(grid_pos, None)
        for client in clients:
            self.children[grid_pos].add_update_client(client, sector_comparer=sector_comparer)

        logger.info(f"child layer added at Lvl {self.lvl}: {grid_pos} with area rect: {child_rect}")

    def _handle_child_layer(self, grid_pos: Tuple[int, int], sector_comparer: rect.RectComparer):

        # capacity has not been reached (mult clients at shared pos are treated as 1). Therefore, we choose not
        # to add a child (or handle). We can return early bc there is not a reason to handle children in this case.
        # Additionally, we do not want to continue if we have reached our max-level depth
        clients = self.ClientMappings.get(grid_pos, None)

        if clients is None \
                or len(clients) <= self.capacity \
                or (self.max_lvls is not None and self.lvl >= self.max_lvls - 1) \
                or self.children.get(grid_pos, None) is not None:
            return False

        # there is no child but capacity is reached. we need to add a child layer to the tree
        if self.children.get(grid_pos, None) is None and len(clients) > self.capacity:
            self._add_child_layer(grid_pos,sector_comparer=sector_comparer)
            return True

        raise ValueError(f"Coding error... Outside the expected two conditions")

    def add_update_client(self, client, sector_comparer: rect.RectComparer):
        if self.lvl == 0:
            logger.info(f"User requests adding [{client}]")

            if not client.__hash__:
                raise Exception(f"Client {client} must be hashable, but type {type(client)} is not")

        # check if can skip since already up to date
        #TODO: This was implemented w. pos, harder in abstract sense

        # check if already have client in but at a different location
        #TODO: This was implemented w. pos, harder in abstract sense


        # Check which grid_pos client belongs to
        found_a_grid = False
        for grid_pos, _ in self.grid.grid_enumerator:
            area = sec_u.sector_rect(sector_dims=sec_u.sector_dims(self._area[2:4],
                                                                   sector_def=self.grid.Shape),
                                     sector=grid_pos,
                                     area_origin=self._area[0:2])
            if sector_comparer(area, client):
                found_a_grid = True
                self._client_mapping.setdefault(grid_pos, set()).add(client)
                logger.info(f"client [{client}] added to Lvl {self.lvl}: {grid_pos}")

                # handle child lvl
                layer_added = self._handle_child_layer(grid_pos, sector_comparer=sector_comparer)

                if not layer_added and self.children.get(grid_pos, None) is not None:
                    self.children[grid_pos].add_update_client(client, sector_comparer=sector_comparer)

        # if not found_a_grid:
        #     raise ValueError(f"")

    def remove_client(self, client):
        # if not a member, early out
        if client not in self._last_mapped_pos.keys():
            return

        logger.info(f"removing client [{client}] from {self.lvl}: {self._last_mapped_pos[client]}")

        # delete from last mapped
        del self._last_mapped_pos[client]

        # delete from client mappings
        for grid_pos, clients in self._client_mapping.items():
            if client in clients:
                clients.remove(client)

        # handle children
        to_remove = []
        for pos, child in self.children.items():
            # remove client from child
            child.remove_client(client)

            #remove child if empty
            positions = set([pos for client, pos in child.ClientsPos.items()])
            if len(positions) <= self.capacity:
                to_remove.append(pos)

        for child in to_remove:
            del self.children[child]

    def _sector_corners_nearby(self, radius: float, pt: Tuple[float, float]):
        ret = {}
        for pos, sector in self.MySectors:
            corners = rect.rect_corners(sector)

            tl = self._within_radius_of_point(corners[CardinalPosition.TOP_LEFT], radius=radius, pt=pt)
            tr = self._within_radius_of_point(corners[CardinalPosition.TOP_RIGHT], radius, pt)
            bl = self._within_radius_of_point(corners[CardinalPosition.BOTTOM_LEFT], radius, pt)
            br = self._within_radius_of_point(corners[CardinalPosition.BOTTOM_RIGHT], radius, pt)
            ret[pos] = sum([tl, tr, bl, br])

        return ret

    def _within_radius_of_point(self, check: Tuple[float, float], radius: float, pt: Tuple[float, float]):
        return vec.distance_between(check, pt) <= radius

    def _sectors_potentially_overlaps_radius(self, radius: float, pt: Tuple[float, float]):
        ret = {}
        for pos, sector_area in self.MySectors:
            ret[pos] = False

            # determine if the bounding circle of my area plus the radius given to check is more than the distance
            # between the center of my area and the point to be checked. If the combined distance of the two radius's is
            # smaller than the distance between center and pt, we can safely assume that the area of the sector does NOT
            # intersect with the area being checked. However if it is larger, there is a potential that the area falls
            # within the checked area
            if rect.bounding_circle_radius(sector_area) + radius >= vec.distance_between(pt, rect.rect_center(sector_area)):
                ret[pos] = True
        return ret

    @property
    def ClientMappings(self) -> Dict[Tuple[int, int], set[Any]]:
        return self._client_mapping

    @property
    def DeepMappings(self) -> Dict[Tuple[int, int], set[Any]]:
        return {
            k: (list(v), self.children[k].Area, self.children[k].DeepMappings) if k in self.children else (list(v), {})
            for k, v in self.ClientMappings.items()
        }

    @property
    def JsonableDeepMappings(self) -> Dict[str, Dict]:
        return {
            str(k): (list(v), self.children[k].Area, self.children[k].JsonableDeepMappings) if k in self.children else (list(v), {})
            for k, v in self.ClientMappings.items()
        }

    @property
    def MySectors(self) -> List[Tuple[Tuple[float, float], rect.Rect]]:
        mine = []
        sec_def = sec_u.rect_sector_attributes((self._area[2], self._area[3]), self.grid.Shape)
        for pos, _ in self.grid.grid_enumerator:
            _rect = (
                pos[1] * sec_def[0] + self._area[0],
                pos[0] * sec_def[1] + self._area[1],
                sec_def[0],
                sec_def[1]
            )

            mine.append((pos, _rect))

        return mine

    @property
    def Sectors(self) -> List[Tuple[Tuple[float, float], rect.Rect]]:
        childrens = []
        for pos, child in self.children.items():
            childrens += child.Sectors

        return self.MySectors + childrens

    @property
    def Area(self) -> rect.Rect:
        return self._area

    def plot(self,
             ax,
             nearby_pt: Tuple[float, float] = None,
             radius: float=None,
             pt_color: Color = None):

        plot_series([point for client, point in self.ClientsPos.items()], ax=ax, color=pt_color, series_type='scatter', zOrder=4)

        if nearby_pt is not None and radius is not None:
            nearbys = self.nearby_clients(pt=nearby_pt, radius=radius)
            # near_x_s = [point[0] for client, point in nearbys.items()]
            # near_y_s = [point[1] for client, point in nearbys.items()]
            plot_series([point for client, point in nearbys.items()], ax=ax, color=pt_color,
                        series_type='scatter', zOrder=4)
            # ax.scatter(near_x_s, near_y_s,)


        for _, sector in self.Sectors:
            rect = patches.Rectangle((sector[0], sector[1]), sector[2], sector[3], linewidth=1, edgecolor='r',
                                     facecolor='none')
            ax.add_patch(rect,)

    @property
    def CoLocatedClients(self) -> Dict:
        ret = {}

        for grid_pos, clients in self.ClientMappings.items():
            gpcc = None

            for client in clients:
                if grid_pos in self.children:
                    ret.setdefault(client, set())

                    if gpcc is None:
                        gpcc = self.children[grid_pos].CoLocatedClients

                    ret[client] = ret[client].union(gpcc[client])
                else:
                    ret[client] = set([x for x in clients if x != client])
        return ret

if __name__ == "__main__":
    from cooptools.randoms import a_string
    import random as rnd
    import matplotlib.pyplot as plt
    import time
    from pprint import pprint
    from cooptools.common import flattened_list_of_lists
    from cooptools.loggingHelpers import BASE_LOG_FORMAT

    logging.basicConfig(format=BASE_LOG_FORMAT, level=logging.INFO)

    rnd.seed(0)

    def area_gen(_rect, max_w = None, max_h = None):
        x = rnd.uniform(_rect[0], _rect[0] + _rect[2] - 1)
        y = rnd.uniform(_rect[1], _rect[1] + _rect[3] - 1)
        w = min(rnd.uniform(x, _rect[2] - 1), max_w if max_w else 100000000000000)
        h = min(rnd.uniform(y, _rect[3] - 1), max_h if max_h else 100000000000000)

        return x, y, w, h

    def test1():
        _rect = (0, 0, 400, 400)
        t0 = time.perf_counter()
        qt = SectorTree(area_rect=_rect,
                        shape=(3, 3),
                        capacity=1,
                        max_lvls=3)

        check_area_1 = (100, 100, 100, 10)
        check_area_2 = (100, 100, 10, 100)
        check_area_3 = (150, 150, 100, 100)

        qt.add_update_client(client="1", sector_comparer=lambda x: rect.overlaps(x, check_area_1))
        qt.add_update_client(client="2", sector_comparer=lambda x: rect.overlaps(x, check_area_2))
        qt.add_update_client(client="3", sector_comparer=lambda x: rect.overlaps(x, check_area_3))

        pprint(qt.DeepMappings)

    def test2():
        _rect = (0, 0, 400, 400)
        t0 = time.perf_counter()
        qt = SectorTree(area_rect=_rect,
                        shape=(3, 3),
                        capacity=1,
                        max_lvls=4)

        check_areas = {
            ii: area_gen(_rect, max_w=100, max_h=100) for ii in range(10)
        }
        pprint(check_areas)
        for ii, check in check_areas.items():
            qt.add_update_client(client=ii, sector_comparer=lambda x, to_check: rect.overlaps(x, check_areas[to_check]))

        dm = qt.DeepMappings
        pprint(dm)

        pprint(qt.CoLocatedClients)
        # for pos, mappings in dm.items():
        #     mine, subs = mappings
        #     all_subbd = flattened_list_of_lists([v[0] for k, v in subs.items()], unique=True)
        #
        #     if any(x not in all_subbd for x in mine):
        #         raise ValueError(f"Missing sUBS!")

    # test1()
    test2()
