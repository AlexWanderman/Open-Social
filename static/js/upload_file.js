function upload_file(url, csrf, file, data) {
    // url - string
    // file - file.files[0]
    // data - map

    const form = new FormData()

    form.append('file', file)
    form.append('data', JSON.stringify(data))

    const xhr = new XMLHttpRequest()

    xhr.open('POST', url)
    xhr.setRequestHeader('X-CSRFToken', csrf)
    xhr.send(form)

    xhr.onreadystatechange = function() {
        if (xhr.readyState != 4) { return }
        console.log(xhr.status + ' | ' + xhr.response)
    }
}

// const file = document.querySelector('#file')
// file.files[0]
// const data = {}
