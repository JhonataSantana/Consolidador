console.log("Calling Python...");
async function teste() {
    let t = await eel.my_python_function(1, 2)();
    console.log(t)
}

teste()

eel.expose(my_javascript_function);
function my_javascript_function(a, b, c, d) {
    if (a < b) {
        console.log(c * d);
    }
}