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
	$('#area-02').empty();
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

};