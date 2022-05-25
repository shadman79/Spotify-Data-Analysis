import requests
import base64, json

authUrl = "https://accounts.spotify.com/api/token"

authHeader = {}

authData = {}

# Base64 encode Client ID and CLient Secret

def getAccessToken(clientId, clientSecret):
    message = f"{clientId}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    authHeader['Authorization'] = "Basic " + base64_message
    authData["grant_type"] = "client_credentials"

    res = requests.post(authUrl, headers=authHeader, data=authData)
    responseObject = res.json()

    accessToken = responseObject["access_token"]

    return accessToken

def getRequest(endpoint, getHeader, p):
    res = requests.get(endpoint, headers=getHeader, params=p)
    resObject = res.json()

    return resObject

def getPlaylist(token, playlistId, p):
    playlistEndpoint = f"https://api.spotify.com/v1/playlists/{playlistId}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(playlistEndpoint, getHeader, p)

def getAlbum(token, albumId, p):
    albumEndpoint = f"https://api.spotify.com/v1/albums/{albumId}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(albumEndpoint, getHeader, p)

def getArtist(token, artistId, info, p):
    artistEndpoint = f"https://api.spotify.com/v1/artists/{artistId}{info}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(artistEndpoint, getHeader, p)

def getTrack(token, trackId, p):
    trackEndpoint = f"https://api.spotify.com/v1/tracks/{trackId}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(trackEndpoint, getHeader, p)

def getAudioFeatures(token, trackId, p):
    featuresEndpoint = f"https://api.spotify.com/v1/audio-features/{trackId}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(featuresEndpoint, getHeader, p)

def itemSearch(token, query, p):
    searchEndpoint = f"https://api.spotify.com/v1/search?{query}"
    searchHeader = {
        "Authorization": "Bearer " + token
    }
    return getRequest(searchEndpoint, searchHeader)