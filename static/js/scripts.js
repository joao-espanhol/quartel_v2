// Função para confirmação de exclusão
function confirmarExclusao(event) {
    const confirmacao = confirm("Tem certeza que deseja excluir este arranchamento?");
    if (!confirmacao) {
        event.preventDefault(); // Impede a exclusão se o usuário cancelar
    }
}

// Adiciona o listener a todos os botões de exclusão
document.addEventListener("DOMContentLoaded", function() {
    const botoesExcluir = document.querySelectorAll(".btn-danger");
    
    botoesExcluir.forEach(function(botao) {
        botao.addEventListener("click", confirmarExclusao);
    });
});

// Função para expandir/contrair o menu de navegação em dispositivos móveis
function toggleMenu() {
    const nav = document.querySelector("nav ul");
    nav.classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.querySelector(".nav-toggle");
    
    if (toggleButton) {
        toggleButton.addEventListener("click", toggleMenu);
    }
});
