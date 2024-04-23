// fetch('/data/luebeck/kommunalwahlkreise_2018.updated.geojson', {
fetch('/data/wahlkreise_gemeinden_2023.geojson', {
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
let prevLayerClicked = null;

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map)


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


let layerStyle = {
    default: {
        color: '#fff',
        fillColor: '#104b44',
        fillOpacity: 0.7,
        opacity: 0.6,
        weight: 2
    },
    click: {
        color: '#fff',
        fillColor: '#06e006',
        fillOpacity: 0.2,
        opacity: 0.4,
        weight: 3
    }
}


function onMapClick(e) {
    const bounds = L.latLngBounds(e.target._bounds._southWest, e.target._bounds._northEast)
    map.fitBounds(bounds)

    const array = e.target.feature.properties.candidates || []
    const list = document.createElement('ul')

    if (array.length === 0) {
        return;
    }

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

    e.preventDefault
}


function onEachFeature(feature, layer) {
    const label = `Wahlkreis ${feature.properties.WK_Name}`

    layer.on('click', function(e) {
        e.target.setStyle(layerStyle.click);

        if (prevLayerClicked !== null) {
            prevLayerClicked.setStyle(layerStyle.default);
        }
        
        const layer = e.target;
        prevLayerClicked = layer;
        
        onMapClick(e)
    })

    layer.bindTooltip(label, {
        permanent: false,
        direction: 'top'
    }).openTooltip()
}


function addData(data) {
    const layer = L.geoJson(data, {
        style: layerStyle.default,
        onEachFeature: onEachFeature
    }).addTo(map)

    map.fitBounds(layer.getBounds(), {padding: [0, 0, 0, 0]})
}
