
from pelicanfs.core import PelicanMap, PelicanFileSystem
import fsspec
import pytest

def test_cat():
    date = '20211016'
    hour = '21'
    var = 'TMP'
    level = '2m_above_ground'
    namespace_file1 = 'chtc/PUBLIC/eturetsky/hrrrzarr/sfc/' + date + '/' + date + '_' + hour + 'z_anl.zarr/' + level + '/' + var + '/' + level +'/.zmetadata'
    namespace_file2 = 'chtc/PUBLIC/eturetsky/hrrrzarr/sfc/' + date + '/' + date + '_' + hour + 'z_anl.zarr/' + level + '/' + var +'/'

    pelfs = PelicanFileSystem("https://osdf-director.osg-htc.org/", asynchronous=False, loop=None)
    url = PelicanMap(namespace_file1, pelfs=pelfs)

    res = pelfs.cat_file(url.root)

    print(res)

    assert False


    #file2 = fs.get_mapper(url2)

    #ds = xr.open_mfdataset([file1, file2], engine='zarr')

    #res = pelfs.ls(url1)

    #print(res)