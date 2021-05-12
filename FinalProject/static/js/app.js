const logo = document.querySelectorAll("#logo path");

for (let i = 00; i < logo.length; i++) {
  console.log(`Letter ${i} is ${logo[i].getTotalLength()}`);
}
