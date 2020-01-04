from opencage.geocoder import OpenCageGeocode
import pandas as pd
import re

API_KEY = '55b4e7b108fa47c28513116997c19dd9'
CITIES_FILE = '../Data/cities.txt'
CRIME_DATASET_FILE = "../Data/CommViolPredUnnormalizedData.txt"

key = API_KEY
geocoder = OpenCageGeocode(key)

columns = ["communityname" , "state" , "countyCode" , "communityCode" , "fold" , "population" , "householdsize" , "racepctblack" , "racePctWhite" , "racePctAsian" , "racePctHisp" , "agePct12t21" , "agePct12t29" , "agePct16t24" , "agePct65up" , "numbUrban" , "pctUrban" , "medIncome" , "pctWWage" , "pctWFarmSelf" , "pctWInvInc" , "pctWSocSec" , "pctWPubAsst" , "pctWRetire" , "medFamInc" , "perCapInc" , "whitePerCap" , "blackPerCap" , "indianPerCap" , "AsianPerCap" , "OtherPerCap" , "HispPerCap" , "NumUnderPov" , "PctPopUnderPov" , "PctLess9thGrade" , "PctNotHSGrad" , "PctBSorMore" , "PctUnemployed" , "PctEmploy" , "PctEmplManu" , "PctEmplProfServ" , "PctOccupManu" , "PctOccupMgmtProf" , "MalePctDivorce" , "MalePctNevMarr" , "FemalePctDiv" , "TotalPctDiv" , "PersPerFam" , "PctFam2Par" , "PctKids2Par" , "PctYoungKids2Par" , "PctTeen2Par" , "PctWorkMomYoungKids" , "PctWorkMom" , "NumKidsBornNeverMar" , "PctKidsBornNeverMar" , "NumImmig" , "PctImmigRecent" , "PctImmigRec5" , "PctImmigRec8" , "PctImmigRec10" , "PctRecentImmig" , "PctRecImmig5" , "PctRecImmig8" , "PctRecImmig10" , "PctSpeakEnglOnly" , "PctNotSpeakEnglWell" , "PctLargHouseFam" , "PctLargHouseOccup" , "PersPerOccupHous" , "PersPerOwnOccHous" , "PersPerRentOccHous" , "PctPersOwnOccup" , "PctPersDenseHous" , "PctHousLess3BR" , "MedNumBR" , "HousVacant" , "PctHousOccup" , "PctHousOwnOcc" , "PctVacantBoarded" , "PctVacMore6Mos" , "MedYrHousBuilt" , "PctHousNoPhone" , "PctWOFullPlumb" , "OwnOccLowQuart" , "OwnOccMedVal" , "OwnOccHiQuart" , "OwnOccQrange" , "RentLowQ" , "RentMedian" , "RentHighQ" , "RentQrange" , "MedRent" , "MedRentPctHousInc" , "MedOwnCostPctInc" , "MedOwnCostPctIncNoMtg" , "NumInShelters" , "NumStreet" , "PctForeignBorn" , "PctBornSameState" , "PctSameHouse85" , "PctSameCity85" , "PctSameState85" , "LemasSwornFT" , "LemasSwFTPerPop" , "LemasSwFTFieldOps" , "LemasSwFTFieldPerPop" , "LemasTotalReq" , "LemasTotReqPerPop" , "PolicReqPerOffic" , "PolicPerPop" , "RacialMatchCommPol" , "PctPolicWhite" , "PctPolicBlack" , "PctPolicHisp" , "PctPolicAsian" , "PctPolicMinor" , "OfficAssgnDrugUnits" , "NumKindsDrugsSeiz" , "PolicAveOTWorked" , "LandArea" , "PopDens" , "PctUsePubTrans" , "PolicCars" , "PolicOperBudg" , "LemasPctPolicOnPatr" , "LemasGangUnitDeploy" , "LemasPctOfficDrugUn" , "PolicBudgPerPop" , "murders" , "murdPerPop" , "rapes" , "rapesPerPop" , "robberies" , "robbbPerPop" , "assaults" , "assaultPerPop" , "burglaries" , "burglPerPop" , "larcenies" , "larcPerPop" , "autoTheft" , "autoTheftPerPop" , "arsons" , "arsonsPerPop" , "ViolentCrimesPerPop" , "nonViolPerPop"]

dataset = pd.read_csv(CRIME_DATASET_FILE, names=columns)

with open(CITIES_FILE, 'w') as f:
    f.write('communityname, state, lat, lng\n')
    for row in dataset.loc[:, ['communityname', 'state']].iterrows():
        
        query_city_name = (row[1]['communityname']
                           .replace('city', '')
                           .replace('township', '')
                           .replace('villeborough', '')
                           .replace('town', '')
                          )
            
        query_city_name = ' '.join(re.findall('[A-Z][a-z]*', query_city_name)) + ', ' + str(row[1]['state'])
    
        print(query_city_name)
        
        query = query_city_name

        results = geocoder.geocode(query)
        
        f.write(str(row[1]['communityname']) + ', ' + str(row[1]['state']) + ', ' 
                + str(results[0]['geometry']['lat']) + ', ' + str(results[0]['geometry']['lng'])  + '\n')