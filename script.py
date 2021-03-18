# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
    'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
    'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
    1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
    175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
    'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
    2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# Update damages function:
def convertDamageData(damages):
    # Dictionary used for converting M/B Values
    conversion = {"M": 1000000, "B":1000000000}
    # empty list to populate updated Damages Values after being converted
    updatedDamages = []

    for damage in damages:
        if damage == "Damages not recorded":
            updatedDamages.append(damage)
        # if the find() method does not return -1 (value not found) execute code 
        if damage.find("M") != -1:
            # add converted value to dictionary as a float by multiplying the value of Key "M"
            updatedDamages.append(float(damage[0:damage.find("M")]) * conversion["M"])
        if damage.find("B") != -1:
            updatedDamages.append(float(damage[0:damage.find("B")]) * conversion["B"])
    return updatedDamages

# call the function and save it to the updated damages list
updatedDamages = convertDamageData(damages)
# Test - Output should be converted values
# print(updatedDamages)

# write your construct hurricane dictionary function here:
def createHurricaneDictionary(names, months, years, max_sustained_winds,areas_affected,updatedDamages, deaths):
    # Empty Dictionary
    hurricanes = {}
    numHurricanes = len(names)

    # Iterate through various lists to get values and add to dictionary
    for i in range(numHurricanes):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Winds": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damages": updatedDamages[i],
            "Death Toll": deaths[i]
        }
    return hurricanes
# Test via calling/printing
hurricanes = createHurricaneDictionary(names, months, years, max_sustained_winds,areas_affected, updatedDamages, deaths)
# print(hurricanes)

# function that creates a dictionary using Year as a Key and returns hurricane values if one occurred that year:
def createYearDictionary(hurricanes):
    # Empty Dictionary to populate in iteration block
    hurricanesByYear = {}

    # Iterate
    for hurricane in hurricanes:
        currentHurricaneYear = hurricanes[hurricane]["Year"]
        currentHurricane = hurricanes[hurricane]
        # Evaluate if the year is present in empty dictrionary, if not, add it
        if currentHurricaneYear not in hurricanesByYear:
            # newDictionaryName[Year Key Value] = hurricane data
            hurricanesByYear[currentHurricaneYear] = currentHurricane
        else :
            hurricanesByYear[currentHurricaneYear] = currentHurricane
    return hurricanesByYear
# Create Dictionary using the new function
hurricanesByYear = createYearDictionary(hurricanes)
# Should print out Last value of every existing list
# print(hurricanesByYear[2018])
# write your count affected areas function here:
def countAffectedAreas(hurricanes):
    affectedAreasCount = {}

    # nested loop - iterate through hurricanes dict and affected_areas list, update count
    for singleHurricane in hurricanes:
        for area in hurricanes[singleHurricane]['Areas Affected']:
            # Evaluate if area is present in affectedAreasCount, if so, increase count
            if area not in affectedAreasCount:
                affectedAreasCount[area] = 1
            else:
                affectedAreasCount[area] += 1
    return affectedAreasCount

# Populate affectedAreasCount dictionary by calling function
affectedAreasCount = countAffectedAreas(hurricanes)
# test if it worked by printing area as key and number of how many areas is present in hurricane dictionary
# print(affectedAreasCount)

# write your find most affected area function here:
def mostAffectedArea(affectedAreasCount):
    # Value will be updated in Evaluation block
    maxAreaCount = 0
    maxArea = ""

    # Iterate through the affectedAreasCount dictionary
    for area in affectedAreasCount:
        # area = key
        if affectedAreasCount[area] > maxAreaCount:
            maxArea = area
            maxAreaCount += affectedAreasCount[area]
    return f"The area with the most affected by hurricanes is {maxArea} with a count of {maxAreaCount} hurricanes"

maxAffectedAreaInfo = mostAffectedArea(affectedAreasCount)
# print(maxAffectedAreaInfo)
# write your greatest number of deaths function here:
def deadliestHurricane(hurricanes):
    deadliestHurricane = ""
    hurricaneDeathCount = 0

    for singleHurricane in hurricanes:
        if hurricanes[singleHurricane]['Death Toll'] > hurricaneDeathCount:
            deadliestHurricane = hurricanes[singleHurricane]['Name']
            hurricaneDeathCount = hurricanes[singleHurricane]["Death Toll"]
    return f"The deadliest hurricane in the dataset is {deadliestHurricane} with {hurricaneDeathCount} deaths"

deadliestHurricaneInfo = deadliestHurricane(hurricanes)
print(deadliestHurricaneInfo)
# write your catgeorize by mortality function here:
def hurricaneMortalityCategory(hurricanes):
    # Mortality dictionary will be used to combine data
    mortalityScale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

    # Declare and initialize new dictionary with mortality scale as key, 
    # and empty list as the value to be populated later
    hurricanesByMortalityRating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    # Iterate through hurricanes and evaluate if their deaths is within a range 
    for singleHurricane in hurricanes:
        totalDeathsByHurricane = hurricanes[singleHurricane]['Death Toll']
        # Evaluate by comapring tDBH var ^ to 
        if totalDeathsByHurricane == mortalityScale[0]:
            hurricanesByMortalityRating[0].append(hurricanes[singleHurricane])
        elif totalDeathsByHurricane > mortalityScale[0] and totalDeathsByHurricane <= mortalityScale[1]:
            hurricanesByMortalityRating[1].append(hurricanes[singleHurricane])
        elif totalDeathsByHurricane > mortalityScale[1] and totalDeathsByHurricane < mortalityScale[2]:
            hurricanesByMortalityRating[2].append(hurricanes[singleHurricane])
        elif totalDeathsByHurricane > mortalityScale[2] and totalDeathsByHurricane <= mortalityScale[3]:
            hurricanesByMortalityRating[3].append(hurricanes[singleHurricane])
        elif totalDeathsByHurricane > mortalityScale[3] and totalDeathsByHurricane <= mortalityScale[4]:
            hurricanesByMortalityRating[4].append(hurricanes[singleHurricane])
        elif totalDeathsByHurricane > mortalityScale[4]:
            hurricanesByMortalityRating[5].append(hurricanes[singleHurricane])
    return hurricanesByMortalityRating

#Test
hurricanesMortalityRating = hurricaneMortalityCategory(hurricanes)
print(hurricanesMortalityRating[4])

# write your greatest damage function here:







# write your catgeorize by damage function here:
