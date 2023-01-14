const selectFileButton = document.getElementById("selectFile");
const sendFileButton = document.getElementById("sendFile");
const fileInput = document.getElementById("fileInput");
const status = document.getElementById("status");


// create a new RTCPeerConnection
const peerConnection = new RTCPeerConnection();

// handle file input change event
fileInput.addEventListener("change", async () => {
    try {
        sendFileButton.style.display = "block";
        const file = fileInput.files[0];
        if (file) {
            status.innerHTML = `Selected file: ${file.name}`;
        } else {
            throw new Error("No file selected");
        }
    } catch (error) {
        console.error(error);
    }
});

// handle send file button click event
sendFileButton.addEventListener("click", async () => {
    const file = fileInput.files[0];
    const channel = peerConnection.createDataChannel("file-sharing");
    channel.onopen = () => {
        channel.send(file);
        status.innerHTML = `File ${file.name} sent!`;
    };
});

// handle data channel message event
peerConnection.ondatachannel = (event) => {
    const channel = event.channel;
    channel.onmessage = (event) => {
        const file = event.data;
        // do something with the received file
    };
};




// handle select file button click event
selectFileButton.addEventListener("click", async () => {
    fileInput.style.display = "block";
});

// handle RTCPeerConnection icecandidate event
peerConnection.onicecandidate = (event) => {
    if (event.candidate) {
        // send the candidate to the other peer using a signaling server
    } else {
        // all candidates have been sent
    }
};

// handle RTCPeerConnection negotiationneeded event
peerConnection.onnegotiationneeded = async () => {
    try {
        // create an offer
        const offer = await peerConnection.createOffer();
        // set the local description
        await peerConnection.setLocalDescription(offer);
        // send the offer to the other peer using a signaling server
    } catch (error) {
        console.error(error);
    }
};

// import io from 'socket.io-client';
const socket = io("http://localhost:3000");


// handle signaling server message event
socket.on("message", async (message) => {
    if (message.type === "offer") {
        // set the remote description
        await peerConnection.setRemoteDescription(new RTCSessionDescription(message));
        // create an answer
        const answer = await peerConnection.createAnswer();
        // set the local description
        await peerConnection.setLocalDescription(answer);
        // send the answer to the other peer using a signaling server
        socket.emit("message", { type: "answer", sdp: answer });
    } else if (message.type === "answer") {
        // set the remote description
        await peerConnection.setRemoteDescription(new RTCSessionDescription(message));
    } else if (message.type === "candidate") {
        // add the candidate to the RTCPeerConnection
        await peerConnection.addIceCandidate(new RTCIceCandidate(message.candidate));
    }
});

// handle RTCPeerConnection icecandidate event
peerConnection.onicecandidate = (event) => {
    if (event.candidate) {
        // send the candidate to the other peer using a signaling server
        socket.emit("message", { type: "candidate", candidate: event.candidate });
    } else {
        // all candidates have been sent
    }
};



channel.onprogress = (event) => {
    const progressBar = document.getElementById("progressBar");
    progressBar.value = event.loaded / event.total * 100;
};


channel.onopen = () => {
    channel.send(file);
    status.innerHTML = `File ${file.name} sent!`;
    channel.close();
};
