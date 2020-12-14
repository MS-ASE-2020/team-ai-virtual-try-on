
export default function (k) {
    return (document.cookie.match("(^|; )" + k + "=([^;]*)") || 0)[2];
}
