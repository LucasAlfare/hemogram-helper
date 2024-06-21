// A constante "data" está no arquivo privado "data.js"

document.body.addEventListener('keypress', (event) => {
  if (event.key === 'f') {
    const pagePatientName = getPatientName();
    console.log(`Starting to handle patient [${pagePatientName}]`);

    const patientData = getDataByPatientName(pagePatientName);

    if (patientData) {
      const fields = getTextFields();
      fillFieldsWithPatientData(fields, patientData);
    } else {
      alert("Erro ao buscar dados do paciente!");
    }
  }
});

function getPatientName() {
  const patientNameElement = document.getElementById("span_atendimento_nome_paciente");
  return patientNameElement.innerText.split(" ", 2).join(" ").toLowerCase();
}

function getDataByPatientName(name) {
  for (const key in data) {
    if (data.hasOwnProperty(key) && key.includes(name)) {
      return data[key];
    }
  }
  return null;
}

function getTextFields() {
  // Seleciona todos os campos de texto com a classe "padrao"
  const textFieldsNodeList = document.querySelectorAll('input[type="text"].padrao');
  // Converte NodeList para array e retorna os primeiros 20 elementos
  return Array.from(textFieldsNodeList).slice(0, 20);
}

function fillFieldsWithPatientData(fields, patientData) {
  for (let i = 0; i < fields.length; i++) {
    let value = "";

    switch (i) {
      case 0:
        value = patientData.Eritrócitos.replace(".", ",");
        break;
      case 1:
        value = formatFieldValue(patientData.Hemoglobina);
        break;
      case 2:
        value = formatFieldValue(patientData.Hematócrito);
        break;
      case 3:
        value = formatFieldValue(patientData.RDW);
        break;
      case 4:
        value = patientData.Leucócitos;
        break;
      case 9:
        value = formatFieldValue(patientData.Neutrófilos);
        break;
      case 10:
        value = formatFieldValue(patientData.Eosinófilos);
        break;
      case 11:
        value = formatFieldValue(patientData.Basófilos);
        break;
      case 12:
        value = formatFieldValue(patientData.Linfócitos);
        break;
      case 14:
        value = formatFieldValue(patientData.Monócitos);
        break;
      case 16:
        value = patientData.Plaquetas;
        break;
      case 17: // VPM
        value = "9.8".replace(".", ",");
        break;
      case 18: // Plaquetócrito
        value = "0.25".replace(".", ",");
        break;
      case 19: // PDW
        value = "15.8".replace(".", ",");
        break;
      default:
        value = "0";
        break;
    }

    fields[i].value = value;
  }
}

function formatFieldValue(value) {
  if (value.length === 2) {
    value = value + ",0";
  }
  return value.replace(".", ",");
}
