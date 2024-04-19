# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:26:26 2021

@author: Michael Nauge, Université de Poitiers
"""
import sys


import pandas as pd

import requests
import json


import nklAPI_Datas as nklD
import nklAPI_Collections as nklC



def collectionToDf(nklTarget, targetCollection):
    
    
    # TODO
    pass
    

def collectionDatasToDf(nklTarget, targetCollection):
    """
    Obtenir toutes les metas des datas d'une collection nakala 
    dont on connait l'identifiant de collection
    

    Parameters
    nklTarget : OBJ
    	une instance d'un objet NklTarget
    
    targetCollection : STR
        un identifier collection nakala.
        ex : '10.34847/nkl.d9b3cp68'

    Returns
    -------
    dfData : DICT
        un dictionnaire contenant les metadatas des datas
        
    dfFile : DICT
        un dictionnaire contenant les metadatas des files des datas

    """   
    
    # exemple d'url de collection à exporter : 
    # https://apitest.nakala.fr/collections/10.34847/nkl.74aa9b31
    
    
    indexPage = 1
    
    lastPage = sys.maxsize

    # creation de la dataframe Datas avec juste les noms de colonnes pour les datas
    dfData = pd.DataFrame(columns=['linkedInCollection','dataIdentifier','uriData','nkl_title','nkl_created','nkl_license','nkl_type', 'nkl_type_converted','creators_formated'])
    
    # creation de la dataframe Files avec juste les noms de colonnes pour les files
    dfFile = pd.DataFrame(columns=['linkedInData','linkedInData_Title','uriData','name','uriFileDL','description','size','extension','sha1','mime_type','embargoed','uriFileEmbed'])
    
    print("start datas collection extraction")

    while indexPage <= lastPage:
        
        
        
        rc = nklC.get_collections_datas(nklTarget, targetCollection, page=indexPage, limit=10)
        indexPage+=1
        
        if rc.isSuccess:
            lastPage = rc.dictVals['lastPage']
            
            print("pagined extraction:", str(indexPage-1)+"/"+str(lastPage))

            
            for data in rc.dictVals['data']:

                dataUri = data["uri"]
                dataUri = dataUri.replace('https://doi.org/','')
                
                print(dataUri,' ', data["status"])
                
                dataTitle = ""
                #'linkedInCollection','dataIdentifier','uriData',
                #'nkl_title','nkl_created','nkl_license','nkl_type', 
                #'nkl_type_converted','creators_formated'
                
                dicRowData = {}
                dicRowData['linkedInCollection'] = ["not yet available in nakalapycon"]
                dicRowData['dataIdentifier'] = [dataUri]
                dicRowData['uriData'] = [nklTarget.BASE_URL+"/"+dataUri]
                dicRowData['nkl_title'] = [""]
                dicRowData['nkl_created'] = [""]
                dicRowData['nkl_license'] = [""]
                dicRowData['nkl_type'] = [""]
                dicRowData['nkl_type_converted'] = [""]
                dicRowData['creators_formated'] = [""]

                
                if 'collectionsIds' in data:
                    print(data["collectionsIds"])
                
                
                for meta in data['metas']:
                    #print(meta['value'], " ", meta['propertyUri'])
                    
                    if meta['propertyUri'] == 'http://nakala.fr/terms#title':
                        #print("title :", meta['value'])
                        dataTitle = meta['value']
                        dicRowData['nkl_title'] = [dataTitle]
                      
                    if meta['propertyUri'] == 'http://nakala.fr/terms#created':
                        dicRowData['nkl_created'] = [meta['value']]
                        
                    if meta['propertyUri'] == 'http://nakala.fr/terms#license':
                        dicRowData['nkl_license'] = [meta['value']]
                      
                    
                    if meta['propertyUri'] == "http://nakala.fr/terms#type":
                        dicRowData['nkl_type'] = [meta['value']]
                        
                        #dicRowData['nkl_type_converted'] = myConst.vocabTypeGetKeyByUri(meta['value'])  
                        dicRowData['nkl_type_converted'] = [""]
                        
                    if meta['propertyUri'] == "http://nakala.fr/terms#creator":
                        
                        #les anciennes data nakala n'avait pas la meme structuration pour le type creator
                        if not (meta['value']==None):
                            
                            if isinstance(meta['value'], dict):
                                formattedName = meta['value']['givenname']+" "+meta['value']['surname']
                                
                                if dicRowData['creators_formated'] == [""]:
                                    dicRowData['creators_formated'] = [formattedName]
                                else:
                                    dicRowData['creators_formated'][0] += ", "+formattedName
                            else:
                                if dicRowData['creators_formated'] == [""]:
                                    dicRowData['creators_formated'] = [meta['value']]
                                else:
                                    dicRowData['creators_formated'][0] += ", "+meta['value']
                                
                             
                #obsolete       
                #dfData = dfData.append(dicRowData, ignore_index=True) 
                dfRowData = pd.DataFrame(data=dicRowData)


                dfData = pd.concat([dfData, dfRowData])
                
                
                for file in data['files']:
                    #print(file['name'], file['extension'],file['size'],file['mime_type'],file['sha1'],file['embargoed'],file['description'])
                    #print(">> uriFile", myConst.API_URL+"/data/"+dataUri+"/"+file['sha1'])
                    #dicRowFile = file.copy()
                    #'linkedInData','linkedInData_Title','uriData',
                    #'name','uriFileDL','description','size','extension',
                    #'sha1','mime_type','embargoed','uriFileEmbed'
                    
                    dicRowFile = {}
                    dicRowFile['linkedInData'] = [dataUri]
                    dicRowFile['linkedInData_Title'] = [dataTitle]
                    dicRowFile['uriData'] = [nklTarget.BASE_URL+"/"+dataUri]
                    dicRowFile['name'] = [file['name']]
                    dicRowFile['uriFileDL'] = [nklTarget.API_URL+"/data/"+dataUri+"/"+file['sha1']]
                    dicRowFile['description'] = [file['description']]
                    dicRowFile['size'] = [file['size']]
                    dicRowFile['extension'] = [file['extension']]
                    dicRowFile['sha1'] = file['sha1']
                    dicRowFile['mime_type'] = file['mime_type']
                    dicRowFile['embargoed'] = file['embargoed']
                    dicRowFile['uriFileEmbed'] = [nklTarget.API_URL+"/embed/"+dataUri+"/"+file['sha1']]
                    
                    #obsolete
                    #dfFile = dfFile.append(dicRowFile, ignore_index=True)
                    dfRowFile = pd.DataFrame(data=dicRowFile)
                    dfFile = pd.concat([dfFile, dfRowFile])                        
        else:
            lastPage = 0

    
    return dfData, dfFile
    

def getImageSize(nklTarget, dataIdentifier, fileIdentifier):
    """
    

    Parameters
    ----------
    nklTarget : OBJ
        une instance d'un objet NklTarget
        
    dataIdentifier : STR
        l'id d'une data qui existe dans le nakala cible
        
        attention : il arrive que l'on cherche une data dans le nakala_production alors 
        qu'elle que cette data n'existe que dans le nakala_test
        
        exemple : dataIdentifier="10.34847/nkl.f1ea3017"
        
    fileIdentifier : STR
        le SHA1 d'un file présent dans la data
        
        exmple : fileIdentifier = "206f92670979917a79a208788e65c2fa4c48634c"

    Returns
    -------
    width : INT
        La largeur d'origine en pixel de l'image cible
    height : INT
       La hauteur d'origine en pixel de l'image cible

    """
    
    width = 0
    height = 0
        
    url = nklTarget.API_URL+"/iiif/"+dataIdentifier+"/"+fileIdentifier+"/info.json"
    
    APIheaders = {}
    if nklTarget.apiKey_isEmpty()==False:
        APIheaders = {"X-API-KEY": nklTarget.API_KEY_NKL} 

    try :
        response = requests.get(url, headers=APIheaders)
        
        if response.status_code == 200:
            dicoR = json.loads(response.text)

            width = dicoR['width']
            height = dicoR['height']
    except :
        e = sys.exc_info()[0]
        print("error ", e)

    
    return width, height
    
    
    
def getImageUrlIIIF(nklTarget, dataIdentifier, fileIdentifier, region, size, rotation, quality, formatExt):
    """
    Obtenir une URL correctement formaté pour que le serveur IIIF image de 
    Nakala puisse répondre correctement.

    Parameters
    ----------
    nklTarget : OBJ
        une instance d'un objet NklTarget
        
    dataIdentifier : STR
        l'id d'une data qui existe dans le nakala cible
        
        attention : il arrive que l'on cherche une data dans le nakala_production alors 
        qu'elle que cette data n'existe que dans le nakala_test
        
        exemple : dataIdentifier="10.34847/nkl.f1ea3017"
        
    fileIdentifier : STR
        le SHA1 d'un file présent dans la data
        
        exmple : fileIdentifier = "206f92670979917a79a208788e65c2fa4c48634c"
        
    region : STR
        la région de l'image que l'on souhaite
        
        exemple : region="3976,3143,870,618" 
        permet une extraction à partir de l'image d'origine d'un rectangle
        commençant au pixel 3976 sur l'axe horizontal, 
        3143 sur l'axe vertical, 
        de dimension de 870 pixels de largeur et 
        618 pixels de hauteur
    
        
    size : STR
        la taille de l'image cible générée en pixels   
        exemple size="full" ou size="800, 600"
        Si on choisit la valeur full, l'image extraite est fournie à 
        la meilleure taille disponible 
        
    rotation : STR
        correspond à un angle de rotation pour l'image cible 
        (en degrés, dans le sens des aiguilles d'une montre; par exemple "90") 
         exemple : rotation  = "0"
        
        
        
    quality : STR
        correspond à l'espace couleur attendu
        valeurs possible : default, gray, bitonal 
        exemple : quality = "default"
        
    formatExt : STR
        correspond au format de fichier attendu
        valeurs possible : png, jpg, jp2, pdf, gif, tif
        exemple : formatExt="formatExt"

    Returns
    -------
    urlImg : STR
        Une URL correctement formaté pour que le serveur IIIF de Nakala
        puisse répondre correctement

    """
    
    urlImg = nklTarget.API_URL+"/iiif/"+dataIdentifier+"/"+fileIdentifier

    urlImg += "/"+region+"/"+size+"/"+rotation+"/"+quality+"."+formatExt

    return urlImg

        

def getSoundTimeDuration(dataIdentifier, fileIdentifier):
    # TODO 
    
    # vivement un IIIF A/V !
    
    # je tente une estimation par la taille du fichier, un bitrate standard et
    # on dit qu'on est en mono ?!
    
    
    duration = 0
    

    return duration
    