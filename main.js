fetch('/data/kommunalwahlkreise_2018.updated.geojson', {
// fetch('https://map.de/query/xxx', {
    method: 'GET'
})
.then((response) => {
    return response.json()
})
.then((data) => {
    addData(data);
})
.catch(function (error) {
    console.log(error);
})


const map = L.map('map').setView([54.7836, 9.4321], 13);


L.tileLayer.wms('https://sgx.geodatenzentrum.de/wms_basemapde?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=de_basemapde_web_raster_grau&WIDTH=512&HEIGHT=512&CRS=EPSG%3A25832&STYLES=&BBOX=442800%2C5809000%2C1231728.7726528377%2C6597928.772652837', {
    layers: 'de_basemapde_web_raster_grau'
}).addTo(map)

/*L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)*/


let geocoder = L.Control.Geocoder.nominatim()

if (typeof URLSearchParams !== 'undefined' && location.search) {
    // parse /?geocoder=nominatim from URL
    let params = new URLSearchParams(location.search)
    let geocoderString = params.get('geocoder')

    if (geocoderString && L.Control.Geocoder[geocoderString]) {
        console.log('Using geocoder', geocoderString)
        geocoder = L.Control.Geocoder[geocoderString]()
    } else if (geocoderString) {
        console.warn('Unsupported geocoder', geocoderString)
    }
}

const osmGeocoder = new L.Control.geocoder({
    query: 'Flensburg',
    position: 'topright',
    placeholder: 'Adresse oder Ort',
    defaultMarkGeocode: false
}).addTo(map)

osmGeocoder.on('markgeocode', e => {
    const bounds = L.latLngBounds(e.geocode.bbox._southWest, e.geocode.bbox._northEast)
    map.fitBounds(bounds)
})


function onMapClick(evt) {
    const bounds = L.latLngBounds(evt.target._bounds._southWest, evt.target._bounds._northEast)
    map.fitBounds(bounds)

    const array = evt.target.feature.properties.candidates
    const list = document.createElement('ul')

    list.classList.add('p-3')

    for (let i = 0; i < array.length; i++) {
        const item = document.createElement('li')
        const candidate = `<strong>${array[i][0]}</strong><br><p>${array[i][1]}, ${array[i][2]}</p>`

        item.classList.add('mb-2')
        item.innerHTML = candidate
        list.appendChild(item)
    }

    document.getElementById('details').innerHTML = ''
    document.getElementById('details').appendChild(list)

    evt.preventDefault
}


function onEachFeature(feature, layer) {
    const label = `Wahlkreis ${feature.properties.NAME}`

    layer.on('click', function(evt) {
        onMapClick(evt)
    })

    layer.bindTooltip(label, {
        permanent: false,
        direction: 'top'
    }).openTooltip()
}


function addData(data) {
    const layer = L.geoJson(data, {
        onEachFeature: onEachFeature
    }).addTo(map)

    map.fitBounds(layer.getBounds(), {padding: [0, 0, 0, 0]})
}
