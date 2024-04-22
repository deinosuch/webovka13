let nevim = 1;
document.querySelector("p").innerHTML = nevim;

let press = () => {
    nevim = nevim + 1;
    document.querySelector("p").innerHTML = nevim;
}