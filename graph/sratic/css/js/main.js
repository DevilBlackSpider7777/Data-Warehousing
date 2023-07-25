//console.log('hello world')
var ws = new Wevsocket('ws://iocalohost:8000/ws/graph')

ws.onmessage = function(e){
    var d = JSON.parse(e.data)
    document.querySelector('#app').innerText = d.value
}