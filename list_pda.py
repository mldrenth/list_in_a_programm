list_of_plants_owned = ["Parlor Palm", "Ponytail Palm", "Polka Dot Plant", "Olive Tree", "Bromeliad", "Rattlesnake Plant"]

def has_plant(plant_list, plant_name):
    if plant_name in plant_list:
        return "Yes, I own this plant!"
    else:
        return "No, I do not own this plant!"

print(has_plant(list_of_plants_owned, "Olive Tree"))
print(has_plant(list_of_plants_owned, "Monstera"))