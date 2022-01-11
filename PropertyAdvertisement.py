import dataclasses


@dataclasses.dataclass
class PropertyAdvertisement:
    # Inserat
    title: str
    description: str
    type: str
    homegate_id: int
    datePosted: str
    #About Property
    category: str
    price: int                    #<div class="SpotlightAttributes_value_2njuM">
    living_space: int             #<div class="SpotlightAttributes_value_2njuM"> or Eckdaten
    plot_area: int                #Eckdaten : <div class="CoreAttributes_coreAttributes_2UrTf" data-v-392d27ad>
    priceCurrency: str
    rooms: int                    #Eckdaten : <div class="CoreAttributes_coreAttributes_2UrTf" data-v-392d27ad>
    features_equipment: str       #Array? <ul class="FeaturesFurnishings_list_1HzQj">

