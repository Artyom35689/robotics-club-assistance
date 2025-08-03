const tg = window.Telegram.WebApp;
tg.expand();

const userId = tg.initDataUnsafe?.user?.id;
document.getElementById("username").innerText = tg.initDataUnsafe?.user?.first_name || "пользователь";

// Запрос к backend API
fetch(`http://localhost:8000/users/${userId}/teams`)
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("teams");
    if (data.length === 0) {
      container.innerText = "Вы не состоите ни в одной команде.";
      return;
    }
    container.innerHTML = "<h3>Ваши команды:</h3><ul>" + 
      data.map(team => `<li>${team.name}</li>`).join("") + "</ul>";
  })
  .catch(err => {
    document.getElementById("teams").innerText = "Ошибка загрузки данных.";
    console.error(err);
  });
