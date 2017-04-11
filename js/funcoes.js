function minhaFuncao1(){
	$('#area-01').css({
		color: '#ff0000',
		textTransform: 'uppercase',
		width: 600
	});
};

function minhaFuncao2(){
	$('#area-02').empty();// Remove todos os elementos filhos daquele cujo id
	var alunos = ['Jose ', 'Malaquias ', 'Beltrano ', 'Babuino ', 'Jacare'];
	//Itera ao longo do array inserindo seus elementos ao final d
	for(i = 0; i < alunos.length; i++){
		$('#area-02').append(alunos[i]);
	}
};

function minhaFuncao3(){
<<<<<<< HEAD
	$('#area-02').empty();
=======
	$('#area-02').empty();//Remove todos os elementos filhos daquele ID 
>>>>>>> 8598cccb4ba590c38f0f27f6f09a527584cc9102
	var alunos = [
		{
			nome: 'Maria',
			idade: 22
		},
		{
			nome: 'Julia',
			idade: 12
		},
		{
			nome: 'Marina',
			idade: 22
		},
		{
			nome: 'Livia',
			idade: 28
		},

	];

	for(i=0; i<5; i++)
	{
		console.log(alunos[i]);
	}

//Itera ao longo do array inserindo seus elementos ao final

	var list = $("#area-02").append('<ul></ul>').find('ul');
	$.each(alunos, function(index, value) {
	list.append('<li>' + value.nome + ' - ' + value.idade + '</li>')});

<<<<<<< HEAD
};
=======
};

function minhaFuncao4(){
    $("p").dblclick(function(){
        $(this).hide();
    });
};

$(document).ready(function(){//quando a página é levantada é chamada a função 4
	minhaFuncao4();
});


function minhaFuncao5(){
	$("#p1").mouseenter(function(){
    	alert("You entered p1!");
	});
};

$(document).ready(function(){//quando a página é levantada é chamada a função 4
	minhaFuncao5();
});

>>>>>>> 8598cccb4ba590c38f0f27f6f09a527584cc9102
