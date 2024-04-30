function generatePDF() {
  let pdf = new jsPDF("p", "pt", "a4");
  let options = { pagesplit: true };

  pdf.addHTML($("body"), options, () => {
    pdf.save("myDocument.pdf");
  });
}

generatePDF();