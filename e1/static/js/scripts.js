const socket = io("/chattings");
const getElementById = (id) => document.getElementById(id) || null;

//* get DOM element
const helloStrangerElement = getElementById("hello_stranger");
const chattingBoxElement = getElementById("chatting_box");
const formElement = getElementById("chat_form");

//* draw functions
const drawHelloStranger = (username) =>
  (helloStrangerElement.innerText = `Hello ${username} Stranger :)`);
const drawNewChat = (message, isMe = false) => {
  const wrapperChatBox = document.createElement("div");
  wrapperChatBox.className = "clearfix";
  let chatBox;
  if (!isMe)
    chatBox = `
    <div class='bg-gray-300 w-3/4 mx-4 my-2 p-2 rounded-lg clearfix break-all'>
      ${message}
    </div>
    `;
  else
    chatBox = `
    <div class='bg-white w-3/4 ml-auto mr-4 my-2 p-2 rounded-lg clearfix break-all'>
      ${message}
    </div>
    `;
  wrapperChatBox.innerHTML = chatBox;
  chattingBoxElement.append(wrapperChatBox);
};

//* global socket handler
socket.on("user_connected", (username) => {
  drawNewChat(`${username} connected!`);
});
socket.on("new_chat", (data) => drawNewChat(`${data.username}: ${data.chat}`));
socket.on("disconnect_user", (username) => drawNewChat(`${username}: bye...`));

//* event callback functions
const handleSubmit = (event) => {
  event.preventDefault();
  const inputValue = event.target.elements[0].value;
  if (inputValue !== "") {
    event.target.elements[0].value = "";
    socket.emit("submit_chat", inputValue);
    drawNewChat(`me : ${inputValue}`, true);
  }
};

//* main logic
function registerEventListener() {
  formElement.addEventListener("submit", handleSubmit);
}

function helloUser() {
  const username = prompt("What is your name?");
  socket.emit("new_user", username);
  socket.once("hello_user", (username) => {
    drawHelloStranger(username);
  });
}

function init() {
  helloUser();
  registerEventListener();
}

init();
