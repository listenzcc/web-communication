document.getElementById("input-1").addEventListener("click", function (e) {
    const content = document.getElementById("textarea-1").value;
    console.log(content);

    {
        const ws = new WebSocket("ws://localhost:9386/?accessToken=123456");

        ws.onopen = function (evt) {
            console.log("Connection open ...");
            ws.send(content);
        };

        ws.onmessage = function (evt) {
            const { data } = evt;
            console.log("Received Message: " + data);

            if (data.startsWith("<Ent>:")) {
                document.getElementById("div-1-ent").innerHTML = data.slice(
                    "<Ent>:".length
                );
            }

            if (data.startsWith("<Dep>:")) {
                document.getElementById("div-1-dep").innerHTML = data.slice(
                    "<Dep>:".length
                );
            }

            if (data.startsWith("<Final>:")) {
                ws.close();
            }
        };

        ws.onclose = function (evt) {
            console.log("Connection closed.");
        };
    }
});
