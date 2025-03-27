async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/NumerosGerados/');
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Erro ao buscar dados: ', error);
    }
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

        colors:['#FF6688']


    }

    let chart = new ApexCharts(el, options);
    chart.render()

}

apiData()


