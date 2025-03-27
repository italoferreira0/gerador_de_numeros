async function fetchData() {
    let response = await fetch('http://127.0.0.1:8000/api/NumerosGerados/');
    let data = await response.json();
    return data;
     
}

async function apiData() {
    dataAPI = await fetchData();
    
    // console.log(dataAPI[2].numeroGerado)

    let el = document.getElementById('grafico');

    const data = dataAPI.map(item => item.numeroGerado);
    const date = dataAPI.map(item => item.dataCriacao);

    let options = {

        chart:{
            type: 'bar',
            height: 350
        },

        series:[
            {
                name: 'Número',
                data: data
            }
            
        ],

        xaxis:{ //Eixo x
            categories:date
        },

        colors:['#2e8b57']


    }

    let chart = new ApexCharts(el, options);
    chart.render()

}

apiData()


