let traffic_light = "red"

switch(traffic_light){
    case "red":
        message = "stop immediately"
        break;
    case "yellow":
        message = "prepare to stop"
        break;
    case "green":
        message="proceed or continue driving"
        break;
    default:
        message="Invalid traffic light color"
}
console.log(message)