# rwmapeditor-exgcdwu

___一个铁锈战争 (Rusted Warfare) 地图编辑 python 库___

![released version](https://img.shields.io/pypi/v/rwmapeditor-exgcdwu.svg)

## 目标

python实现铁锈地图文件地块编辑和宾语编辑。

暂时不打算接触地块集。

重点减轻城市争夺地图的宾语编辑工作量

基本框架已完成。

地块组框架已完成。

## 安装

```console
pip install rwmapeditor-exgcdwu
```

## 使用之前

1.使用地图编辑器(Tiled,notTiled)创建新地图，确定大小。

2.手动载入地块集

3.手动创建所需的地块层和宾语层

4.即可使用python库自动改变地块和宾语

## 简易使用例子

```python
# coding: utf-8
import rwmap as rw

rwmap_dir = 'D:/Game/steam/steamapps/common/Rusted Warfare/mods/maps/'
youmap_dir = 'D:/Game/steam/steamapps/common/Rusted Warfare/mods/maps/'
map_name = '[p2]example_skirmish_(2p).tmx'
map_name_out = '[p2]example_skirmish_(2p)(1).tmx'
mygraph:rw.RWmap = rw.RWmap.init_mapfile(youmap_dir + map_name, rwmap_dir)
print(mygraph)

mygraph.addObject(
    "Triggers", 
    {"id": "100", "name": "刷兵实验", "type": "unitAdd", "x": "1500", "y":"1000", "width": "20", "height": "20"}, 
    {"resetActivationAfter":"5s", "spawnUnits": "heavyTank*10", "team" :"0", "warmup":"5s"})

mygraph.addTile("Ground", rw.Coordinate(1, 0), "Long Grass", rw.Coordinate(0, 0))
mygraph.addTile("Ground", rw.Coordinate(2, 0), "Long Grass", rw.Coordinate(0, 0))
mygraph.addTile("Ground", rw.Coordinate(0, 1), "Long Grass", rw.Coordinate(0, 0))

mygraph.addTile_square("Ground", rw.Rectangle(rw.Coordinate(5, 5), rw.Coordinate(10, 10)), "Deep Water", rw.Coordinate(0, 0))

mygraph.addTile_group(rw.Coordinate(5, 20), rw.data.tile_group_grid.fill_tile_group_one_ground_water_28_24)

mygraph.write_file(youmap_dir + map_name_out)

```
