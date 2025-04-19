from faker import Faker
import carstack
from carstack.rest import ApiException


fake = Faker()

configuration = carstack.Configuration(host="http://localhost:8000")

with carstack.ApiClient(configuration) as api_client:
    # Create a manufacturer instance
    manufacturer_request = carstack.ManufacturerRequest(
        brand=fake.company(), country=fake.country()
    )
    manufacturer_api = carstack.ManufacturersApi(api_client)
    try:
        mangufacturer = manufacturer_api.manufacturers_create(manufacturer_request)
    except ApiException as e:
        print("Exception when calling ManufacturersApi->manufacturers_create: %s\n" % e)

    # Create a list of features
    features_ids = []
    feature_api = carstack.FeaturesApi(api_client)
    for _ in range(3):
        feature_request = carstack.FeatureRequest(
            name=fake.word(), description=fake.text()
        )
        try:
            feature = feature_api.features_create(feature_request)
            features_ids.append(feature.id)
        except ApiException as e:
            print("Exception when calling FeaturesApi->features_create: %s\n" % e)

    # Create an instance of the API class
    api_instance = carstack.CarsApi(api_client)
    car_request = carstack.CarRequest(
        body_type=carstack.BodyTypeEnum.SEDAN,
        manufacturer_id=mangufacturer.id,
        features_ids=features_ids,
        model_name=fake.word(),
        year=int(fake.year()),
        price=f"{fake.random_int(min=5000, max=10000)}",
        color=fake.color(),
        mileage=fake.random_int(min=0, max=200000),
        rating=fake.random_int(min=1, max=10), # This will be ignored with v1
    )

    try:
        api_response = api_instance.cars_create(car_request)
    except Exception as e:
        print("Exception when calling CarsApi->cars_create: %s\n" % e)
