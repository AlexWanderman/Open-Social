// Обмен данными с серверов в формате JSON
async function exchange_json(url, data, csrf_token) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify(data),
    })

    if (response.ok) {
        return await response.json()
    }

    return {'status': 'Error! ' + response.status + ' ' + response.statusText}
}
