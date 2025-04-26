document.addEventListener('DOMContentLoaded', () => {
    fetch('cars.json')
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById('cars-table');

            // Добавляем заголовки столбцов
            let headersRow = '<tr><th>Марка</th><th>Модель</th><th>Год выпуска</th></tr>';
            table.innerHTML += headersRow;

            data.forEach(car => {
                let row = `<tr>
                            <td>${car.brand}</td>
                            <td>${car.model}</td>
                            <td>${car.year}</td>
                          </tr>`;
                table.innerHTML += row;
            });
        })
        .catch(error => console.error('Ошибка:', error));
});