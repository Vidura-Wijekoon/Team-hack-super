import json

def writeToJSON(path='',filename,data):
    if(len(path)==null):
        begin=""
    else:
        begin="/"
    filePath =begin+path+ filename+'.json'
    with open(filePath,'w') as fp:
        json.dump(data,fp)

tab1
 exchange_rate_buying= 186.262846///the exchange rate buying
 exchange_rate_selling = 190.402215/// the exchange rate selling
 liquidity= 0.960707	///the liquidty

tab 2
egv = 587,000,000.00/// exports gross value
igv = 994,000,000.00/// imports gross value

tab3
 l_q= 145,000,000.00///Local Quantity
 f_q= 135,000,000.00///Foriegn Quantity

tab4
 r_gdp_c= 431.80/// Remittancec GDP Change

tab5
 a_e= 850,000,000.00/// Apparel Exports

########################################################

data = {
   "Tab 1":
    {
        "Exchange Rate":{
            "Buying":exchange_rate_buying,
            "Selling" : exchange_rate_selling
        },
        "Liquidity":liquidity
    },

    "Tab 2":
    {
        "Exports Gross Value":egv,
        "Imports Gross Value":igv
    },
    
    "Tab 3":
    {
        "Local Quantity":l_q,
        "Foreign Quantity":f_q
    },

    "Tab 4":
    {
        "Remittance GDP Change":r_gdp_c
    },

    "Tab 5":
    {
        "Apparel Exports":a_e
    }

}



### writes json file

writeToJSON('sse','nkn',data)
