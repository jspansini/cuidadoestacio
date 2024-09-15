(function(win,doc){
'use strict';
if(doc.querySelector('.btnDel')){
    let btnDel = doc.querySelectorAll('.btnDel');
    for(let i=0; i < btnDel.length; i++){
        btnDel[i].addEventListener('click', function(event)
        {
            if(confirm('Confirmar remoção da tarefa?')){
                return true;
            }else{
                event.preventDefault();
            }
        });
    }
}

if (document.querySelector('#form')) {
    let form = document.querySelector('#form');

    function sendForm(event) {
        event.preventDefault();  // Previne o comportamento padrão

        let data = new FormData(form);
        let ajax = new XMLHttpRequest();
        let token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;  // CSRF token

        ajax.open('POST', form.action, true);  // Certifique-se que a chamada é assíncrona

        ajax.setRequestHeader('X-CSRF-TOKEN', token);

        ajax.onreadystatechange = function() {
            if (ajax.readyState === 4) {  // Verifica se a requisição terminou
                if (ajax.status === 200) {  // Verifica se a resposta foi bem-sucedida
                    let result = document.querySelector('#result');
                    result.innerHTML = 'Cadastro realizado com sucesso!';
                    result.classList.add('alert', 'alert-success');
                } else {
                    // Se não for 200, exiba um erro na página
                    let result = document.querySelector('#result');
                    result.innerHTML = 'Ocorreu um erro no cadastro.';
                    result.classList.add('alert', 'alert-danger');
                }
            }
        };

        ajax.onerror = function() {
            // Em caso de erro na requisição
            let result = document.querySelector('#result');
            result.innerHTML = 'Erro de rede ou servidor.';
            result.classList.add('alert', 'alert-danger');
        };

        ajax.send(data);
        form.reset();  // Limpa o formulário após o envio
    }

    form.addEventListener('submit', sendForm, false);
}



})(window, document);