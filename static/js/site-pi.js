let btnNext = document.querySelector(".next");
let btnBack = document.querySelector(".back");

let cardAll = document.querySelector("#fundo-assuntos #assuntos");
let container = document.querySelector("#fundo-assuntos");


btnNext.onclick = () => moveCardOnClick("next");
btnBack.onclick = () => moveCardOnClick("back");

function moveCardOnClick(type) {
  let cards = document.querySelectorAll(".materias");

  if (type === "next") {
    cardAll.appendChild(cards[0]);
    container.classList.add("next");
  } else {
    cardAll.prepend(cards[cards.length - 1]);
    container.classList.add("back");
  }

  setTimeout(() => {
    container.classList.remove("next");
    container.classList.remove("back");
  }, 500);
}
