const filters = document.querySelectorAll("[data-filter]");
const cards = document.querySelectorAll(".center-card");
const matchCards = document.querySelectorAll("[data-result]");
const matchResult = document.querySelector(".match-result");

const faqEntities = Array.from(document.querySelectorAll(".faq details")).map((item) => ({
  "@type": "Question",
  name: item.querySelector("summary")?.textContent.trim(),
  acceptedAnswer: {
    "@type": "Answer",
    text: item.querySelector("p")?.textContent.trim(),
  },
}));

if (faqEntities.length) {
  const faqSchema = document.createElement("script");
  faqSchema.type = "application/ld+json";
  faqSchema.id = "faq-schema";
  faqSchema.textContent = JSON.stringify({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "@id": "https://brand-north-delivery.github.io/indiana-detox-guide/#faq",
    url: "https://brand-north-delivery.github.io/indiana-detox-guide/#faq",
    name: "Indiana detox frequently asked questions",
    mainEntity: faqEntities,
  });
  document.head.append(faqSchema);
}

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
