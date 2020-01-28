import pymysql
import xlrd


def connectToDB():
    db = pymysql.connect(
        host="ethan.cikeys.com",
        user="ethancik_root",
        passwd="Rebels1997!",
        database="ethancik_borderlands")
    cursor = db.cursor()
    return cursor


def getManufacturerId(manu_name_param):
    switcher = {
        'Bandit': 1,
        'Dahl': 2,
        'Hyperion': 3,
        'Jakobs': 4,
        'Maliwan': 5,
        'Tediore': 6,
        'Torgue': 7,
        'Vladof': 8,
        'Shredifier': 9,
        'Pangolin': 11,
        'Anshin': 10,
        'Eridian': 14
    }
    return switcher.get(manu_name_param, 'No Manufacturer')
def getLocationID(location_name_param):
    switcher = {
        "Arid Nexus - Badlands": 1	,
        "Arid Nexus - Boneyard": 2	,
        "Bloodshot Ramparts": 3	,
        "Bloodshot Stronghold": 4	,
        "The Bunker": 5	,
        "Caustic Caverns": 6	,
        "Control Core Angel": 7	,
        "The Dust": 8	,
        "End of the Line": 9	,
        "Eridium Blight": 10	,
        "Fink's Slaughterhouse": 11	,
        "Friendship Gulag": 12	,
        "Frostburn Canyon": 13	,
        "Helios (moonbase)": 14	,
        "Hero's Pass": 15	,
        "Lynchwood": 16	,
        "Natural Selection Annex": 17	,
        "Opportunity": 18	,
        "Ore Chasm": 19	,
        "The Raid on Digistruct Peak": 20	,
        "Sanctuary": 21	,
        "Sanctuary Hole": 22	,
        "Sawtooth Cauldron": 23	,
        "Southern Shelf": 24	,
        "Southern Shelf - Bay": 25	,
        "Southpaw Steam & Power": 26	,
        "Terramorphous Peak": 27	,
        "The Fridge": 28	,
        "The Highlands": 29	,
        "The Holy Spirits": 30	,
        "Thousand Cuts": 31	,
        "Three Horns - Divide": 32	,
        "Three Horns - Valley": 33	,
        "Tundra Express": 34	,
        "Vault of the Warrior": 35	,
        "Wildlife Exploitation Preserve": 36	,
        "Windshear Waste": 37,
        "Any Location": 39,
        "Hayters Folly": 40,
        'Badasscrater of Badassitude': 41,
        'Pangolin': 42,
        'Wurmwater': 43,
        'The Winged Storm': 44,
        'Flamerock Refuge': 45,
        'Hunters Grotto': 46,
        'Pyro Petes Bar': 47,
        'DLC Regions': 48,
        'Magnys Lighthouse': 49

    }
    return switcher.get(location_name_param, '-1')

if __name__ == "__main__":
    cursor = connectToDB()

    wb = xlrd.open_workbook('C:\\Users\\Ethan\\Borderlands2Project\\CSVs\\Master Mod List.xlsx')
    sheet = wb.sheet_by_index(0)
    counter = 0
    #TODO: Update weapon table to have location table and grab location ID with python switch case

    for i in range(sheet.nrows):
        if i != 0:
            manu_id_p = getManufacturerId(sheet.cell_value(i,4))
            location_id_p = getLocationID(sheet.cell_value(i, 8).replace('\'', ''))

        # split[0] = sheet.cell_values(i,0)
        # split[1] = sheet.cell_values(i,1)
        # split[2] = sheet.cell_values(i,2)
        # spit[3] = sheet.cell_values(i,3)
        # split[4] = sheet.cell_values(i,4)
        # split[5] = sheet.cell_values(i,5) , damage type
        # split[6] = dropped by sheet.cell_values(i,6)
        # split[7] = min Task, sheet.cell_value(i,7)
        # split[8] = location, sheet.cell_value(i,8)
        # split[9] = rarity, sheet.cell_value(i,9)

            query = "insert into class_mod(manu_id, location_id, item_type, mod_name,mod_perk,manufacturer,location_name,damage_type, dropped_by, minimum_task, rarity, " \
                "dlc) value(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
            cursor.execute(query, (manu_id_p,
                               location_id_p,
                               sheet.cell_value(i,1),
                               sheet.cell_value(i,2),
                               sheet.cell_value(i,3),
                               sheet.cell_value(i,4),
                               sheet.cell_value(i,8),
                               sheet.cell_value(i,5),
                               sheet.cell_value(i,6),
                               sheet.cell_value(i,7),
                               sheet.cell_value(i,9),
                               sheet.cell_value(i,0)))
            cursor.connection.commit()
            print('Finished: ' + sheet.cell_value(i,4))