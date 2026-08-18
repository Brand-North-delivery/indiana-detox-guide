const filters = document.querySelectorAll("[data-filter]");
const cards = document.querySelectorAll(".center-card");
const matchCards = document.querySelectorAll("[data-result]");
const matchResult = document.querySelector(".match-result");

filters.forEach((filter) => {
  filter.addEventListener("click", () => {
    const tag = filter.dataset.filter;

    filters.forEach((item) => item.classList.remove("is-active"));
    filter.classList.add("is-active");

    cards.forEach((card) => {
      const show = tag === "all" || card.dataset.tags.split(" ").includes(tag);
      card.classList.toggle("is-hidden", !show);
    });
  });
});

matchCards.forEach((card) => {
  card.addEventListener("click", () => {
    matchCards.forEach((item) => item.classList.remove("is-selected"));
    card.classList.add("is-selected");
    matchResult.textContent = card.dataset.result;
  });
});
