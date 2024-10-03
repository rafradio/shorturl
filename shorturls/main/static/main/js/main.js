let urlButton = document.getElementById("URL");

urlButton.onclick = async () => {
    let url = new URL(window.location.href);
    url.pathname = "/getdata";
    let csrftoken = getCookie('csrftoken');
    await makeRequest(url, csrftoken);
}

const makeRequest = async (url, csrftoken) => {
    let dataToSend = {'data': document.getElementById("Uname").value};
    const request = new Request(url, {
                                method: "POST",
                                headers: {
                                            'Content-Type': 'application/json;charset=utf-8',
                                            'X-CSRFToken': csrftoken,
                                        },
                                body: JSON.stringify(dataToSend)
                                });
    try {
        const response = await fetch(request);  
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const data = await response.json();
        // console.log("url result = ", data.data);
        // document.getElementById("UResult").value = data.data;
        // document.getElementById("Uname").value = "";
        console.log(data);
    }
    catch(error) {
        console.log(error.message);
    }
    
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        console.log("coockies = ", document.cookie);
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        console.log("coockies = ", cookieValue);
    }
    return cookieValue;
}