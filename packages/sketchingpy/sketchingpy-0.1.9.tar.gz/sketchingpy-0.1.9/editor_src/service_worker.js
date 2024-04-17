const localRequestsChannel = new BroadcastChannel("localRequests");
const localResponseChannel = new BroadcastChannel("localResponses");


const pendingRequests = new Map();
const CACHE_NAME = "sketchbook-cache-20240416";


function getRequiresNetwork(request) {
    const url = new URL(request.url);
    const isIndex = url.pathname === "index.html" || url.pathname === "/";
    const isSketch = url.pathname === "sketch.html";
    const isServiceWorker = url.pathname === "service_worker.js";
    const isNested = url.pathname.substring(1, url.pathname.length).indexOf("/") != -1;
    const exceptions = [isIndex, isServiceWorker, isNested, isSketch];
    const numExceptions = exceptions
        .filter((x) => x == true);
    return numExceptions.length > 0;
}


async function interceptRequest(request) {
    const url = new URL(request.url);
    const currentHost = self.location.hostname;

    let future = null;
    if (currentHost !== url.hostname) {
        future = fetch(url.pathname).then(async (networkResponse) => {
            return networkResponse;
        });
    } else if (getRequiresNetwork(request)) {
        const cache = await caches.open(CACHE_NAME);

        const makeCachedRequest = () => {
            return fetch(request).then(async (networkResponse) => {
                if (url.hostname === currentHost && networkResponse.ok && request.method === "GET") {
                    cache.put(url.pathname, networkResponse.clone());
                }
                return networkResponse;
            });
        }

        future = cache.match(url.pathname).then((cachedValue) => {
            if (cachedValue !== undefined) {
                return new Promise((resolve) => {
                    resolve(cachedValue);
                });
                makeCachedRequest();
            } else {
                return makeCachedRequest();
            }
        });
        
    } else {
        future = new Promise((resolve) => {
            const callback = (response) => resolve(response);
            pendingRequests.set(url.pathname, callback);
            localRequestsChannel.postMessage({"name": url.pathname});
        });
    }

    return (await future);
}


self.addEventListener("fetch", (event) => {
    const request = event.request;
    event.respondWith(interceptRequest(request));
});


localResponseChannel.addEventListener("message", (event) => {
    const callback = pendingRequests.get(event.data.name);
    if (event.data.content !== null) {
        const response = new Response(event.data.content);
        callback(response);
    } else {
        fetch(event.data.name).then((response) => callback(response));
    }
});
