function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}
console.log("jesus")

function render_grafico(url){
    fetch(url,{
        method: 'get',
    }).then(function(result){
        return result.json();
    }).then(function(data){
        const ctx = document.getElementById("grafico").getContext('2d');
        var cores = gera_cor(7);
        const MyChart = new Chart(ctx,{
            type:'bar',
            data:{
               labels: data["categorias"],
               datasets: [{
                label:data["valores"],
                data: data["porcentagem"],
                backgroundColor: cores[0],
                borderColor: cores[1],
                borderWidth: 1

               }]

            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })


    })
}