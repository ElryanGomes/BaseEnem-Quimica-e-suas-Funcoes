function loadQuestionList() {
    const year = document.getElementById("year").value;
    const questionSelect = document.getElementById("question");
    const examButton = document.getElementById("exam-button"); // Botão fixo no HTML

    // Limpar a lista de questões anterior
    questionSelect.innerHTML = '<option value="">-- Selecione --</option>';

    // Verifica se há um link disponível para o ano selecionado
    if (year && questionsData[year]) {
        const questions = questionsData[year];

        // Adicionar opções ao dropdown de questões
        questions.forEach((q, index) => {
            const option = document.createElement("option");
            option.value = index;
            option.textContent = `Questão ${q.id}`;
            questionSelect.appendChild(option);
        });

        // Atualizar o botão se houver um link no JSON
        // Atualizar o botão se houver um link no JSON
        if (questionsData[year][0] && questionsData[year][0].examLink) {
            examButton.style.display = "block";
            examButton.setAttribute("href", questionsData[year][0].examLink);
            examButton.querySelector("button").innerText = `Abrir Prova Completa (${year})`;
        } else {
            examButton.style.display = "none";
        }

    } else {
        questionSelect.innerHTML = '<option value="">-- Nenhuma questão disponível --</option>';
        examButton.style.display = "none";
    }
}

// Carregar questão selecionada
function loadQuestion() {
    const year = document.getElementById("year").value;
    const questionIndex = document.getElementById("question").value;
    const container = document.getElementById("question-container");
    const feedback = document.getElementById("feedback");
    const explanation = document.getElementById("explanation");
    const aiResponseContainer = document.getElementById("ai-response");
    const showAIResponseButton = document.getElementById("show-ai-response");
    const sourceText = document.getElementById("source-text");

    // Limpar a resposta da IA ao carregar uma nova questão
    aiResponseContainer.innerHTML = "";

    // Esconde o botão para resposta da IA
    showAIResponseButton.style.display = "none";

    if (!year || questionIndex === "") {
        alert("Por favor, selecione um ano e uma questão.");
        return;
    }

    const question = questionsData[year][questionIndex];

    // Atualizar o título da questão
    document.getElementById("question-title").innerText = `Questão ${question.id} de ${year}`;


    // Texto principal (suportando HTML com formatação)
    document.getElementById("text1").innerHTML = question.question;

    // Imagem opcional
    const questionImage = document.getElementById("question-image");
    if (question.image) {
        questionImage.src = question.image;
        questionImage.style.display = "block";
    } else {
        questionImage.style.display = "none";
    }

    // Texto 2 opcional (com suporte a HTML)
    const text2 = document.getElementById("text2");
    if (question.text2) {
        text2.innerHTML = question.text2;
        text2.style.display = "block";
    } else {
        text2.style.display = "none";
    }

    const optionsDiv = document.getElementById("options");
    optionsDiv.innerHTML = "";
    feedback.innerText = "";
    explanation.classList.add("hidden");
    const letters = ["a", "b", "c", "d", "e"];
    // Criar opções (imagem ou texto) para a questão
    question.options.forEach((opt, index) => {
        const optionContainer = document.createElement("div");
        optionContainer.style.marginBottom = "15px";
        const letter = String.fromCharCode(65 + index);
        if (opt.image) {
            const img = document.createElement("img");
            img.src = opt.image;
            img.alt = `Imagem da alternativa ${index + 1}`;
            img.style.cursor = "pointer";
            img.style.maxWidth = "100%";
            img.style.height = "auto";
            img.style.border = "2px solid transparent";
            img.onclick = () => checkAnswer(index, question);

            img.onmouseover = () => (img.style.border = "2px solid blue");
            img.onmouseout = () => (img.style.border = "2px solid transparent");

            optionContainer.appendChild(img);
        } else if (opt.text) {
            const button = document.createElement("button");
            button.innerText = `${letters[index]}) ${opt.text}`;
            button.onclick = () => checkAnswer(index, question);
            optionContainer.appendChild(button);
        }

        optionsDiv.appendChild(optionContainer);
    });

    // Carregar vídeo
    const videoContainer = document.getElementById("video-container");
    const videoFrame = document.getElementById("video");
    if (question.video) {
        videoFrame.src = question.video;
        videoContainer.style.display = "block";
    } else {
        videoFrame.src = "";
        videoContainer.style.display = "none";
    }

    if (question.source) {
        sourceText.innerHTML = `<strong>Fonte:</strong> <a href="${question.source}" target="_blank">${question.source}</a>`;
        sourceText.style.display = "block";
    } else {
        sourceText.style.display = "none";
    }

    document.getElementById("tooltip-container").style.display = "none"; // Esconder tooltip ao trocar de questão

    container.classList.remove("hidden");
    container.scrollIntoView({ behavior: "smooth" });
}


function checkAnswer(selected, question) {
    const feedback = document.getElementById("feedback");
    const explanation = document.getElementById("explanation");
    const explanationText = document.getElementById("explanation-text");
    const showAIResponseButton = document.getElementById("show-ai-response");
    const tooltipContainer = document.getElementById("tooltip-container");

    // Pegando todas as alternativas
    const optionsDiv = document.getElementById("options");
    const buttons = optionsDiv.querySelectorAll("button, img");

    // Resetando todas as alternativas para a cor original
    buttons.forEach(btn => {
        btn.style.backgroundColor = "#e6f2ff";
        btn.style.color = "#004080";
        btn.style.border = "2px solid #004080"; // Borda original
    });

    // Pegando a alternativa selecionada
    const selectedOption = buttons[selected];

    // Se a resposta estiver correta
    if (selected === question.correct) {
        feedback.innerText = "Correto!";
        feedback.style.color = "green";
        selectedOption.style.backgroundColor = "green";
        selectedOption.style.color = "white";
        selectedOption.style.border = "3px solid darkgreen";
    } else {
        // Se a resposta estiver incorreta
        feedback.innerText = "Incorreto!";
        feedback.style.color = "red";
        selectedOption.style.backgroundColor = "red";
        selectedOption.style.color = "white";
        selectedOption.style.border = "3px solid darkred";
    }

    // Exibir explicação
    explanation.classList.remove("hidden");
    explanationText.innerHTML = question.explanation;

    // Exibe o botão para a IA responder, caso ainda não esteja visível
    if (showAIResponseButton.style.display === "none") {
        showAIResponseButton.style.display = "block";
        showAIResponseButton.innerText = "Ver Resposta da IA";
    }

    // Torna o tooltip visível após a primeira interação
    tooltipContainer.style.display = "inline-block";

    // Salva a questão atual para a IA responder
    window.currentQuestion = question;
}

function fetchAIResponse() {
    const aiResponseContainer = document.getElementById("ai-response");
    const showAIResponseButton = document.getElementById("show-ai-response");

    if (!window.currentQuestion) {
        aiResponseContainer.innerHTML = "<strong>Erro:</strong> Nenhuma questão foi selecionada.";
        return;
    }

    aiResponseContainer.innerText = "Carregando resposta da IA...";
    const payload = {
        question_text: window.currentQuestion.question,
        text2: window.currentQuestion.text2 || null,
        image: window.currentQuestion.image || null,
        options: window.currentQuestion.options || [],
        correct: window.currentQuestion.correct
    };

    fetch("/ia-response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao obter resposta da IA");
            }
            return response.json();
        })
        .then(data => {
            if (data.ai_response) {
                aiResponseContainer.innerHTML = `<strong>Resposta da IA:</strong> ${data.ai_response}`;

            } else {
                aiResponseContainer.innerHTML = "<strong>Erro:</strong> Não foi possível obter a resposta da IA.";
            }

            // Atualiza o botão para "Gerar outra resposta"
            showAIResponseButton.innerText = "Gerar outra resposta";
        })
        .catch(error => {
            aiResponseContainer.innerHTML = `<strong>Erro:</strong> ${error.message}`;
        });
}





let questionsData = {};

fetch("static/ArquivoJson/questions.json")
    .then(response => {
        if (!response.ok) {
            throw new Error("Não foi possível carregar o arquivo questions.json");
        }
        return response.json();
    })
    .then(data => {
        questionsData = data;
        console.log("Dados carregados:", questionsData);
    });
