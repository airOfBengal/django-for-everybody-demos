import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Iso, Region, State

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()

    for row in reader:
        print(row)

        category, _ = Category.objects.get_or_create(name=row[7])
        state, _ = State.objects.get_or_create(name=row[8])
        region, _ = Region.objects.get_or_create(name=row[9])
        iso, _ = Iso.objects.get_or_create(name=row[10])

        site_name = row[0]
        site_desc = row[1]
        site_just = row[2]
        site_year = row[3]

        try:
            site_year = int(site_year)
        except:
            site_year = None

        site_long = row[4]
        try:
            site_long = float(site_long)
        except:
            site_long = None

        site_lat = row[5]
        try:
            site_lat = float(site_lat)
        except:
            site_lat = None

        site_area = row[6]
        try:
            site_area = float(site_area)
        except:
            site_area = None

        site = Site(name=site_name, year=site_year,
        description=site_desc, justification=site_just,
        longitude=site_long, latitude=site_lat, area_hectares=site_area,
        category=category, state=state, region=region, iso=iso)

        site.save()


