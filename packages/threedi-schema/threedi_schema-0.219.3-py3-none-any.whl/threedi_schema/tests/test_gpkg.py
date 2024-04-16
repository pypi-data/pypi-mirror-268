from threedi_schema.domain import models


def test_read_geometry(gpkg_db):
    channel = gpkg_db.get_session().query(models.Culvert).first()
    assert channel.code == "40902275"
    assert channel.the_geom is not None  # this is what happens with GeoAlchemy2
