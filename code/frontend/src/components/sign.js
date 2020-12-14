
import axios from 'axios'
import getCookieName from './GetCookie'

export default {
  in(signInData, isSaler) {
    let url = ""
    if (isSaler) {
      url += "/api/saler/login";
    } else {
      url += "/api/customer/login";
    }
    axios
      .post(url, signInData, {
        headers: {
          "X-CSRFToken": getCookieName("csrftoken"),
        },
      })
      .then((response) => {
        console.log(response);
        // confirm("Sign in successfully!");
        let data = response.data;

        localStorage.setItem("name", data.name);
        if (isSaler) {
          localStorage.setItem("isSaler", "y");
          window.location.href = "/salerinfo";
        } else {
          localStorage.setItem("isSaler", "n");
          window.location.href = "/customerinfo";
        }
      })
      .catch((error) => {
        if (error.response.status === 400) {
          alert("Invalid name or password!")
        }
        else {
          alert(error);
        }
      });
  },
  out() {
    try {
      let id = localStorage.getItem("isSaler");
      if (id === "n") {
        axios.get("/api/customer/logout");
      } else if (id === "y") {
        axios.get("/api/saler/logout");
      }
    } catch (error) {
      console.log(error);
      alert(error);
      return;
    }
    localStorage.clear();
    window.location.href = "/";
  },
  up(signUpData, isSaler, file) {
    const formData = new FormData();

    Object.keys(signUpData).forEach((key) =>
      formData.append(key, signUpData[key])
    );
    let url = "";
    if (isSaler) {
      url += "/api/saler/signup";
    } else {
      url += "/api/customer/signup";
      formData.append("self_pics", file);
    }
    axios
      .post(url, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRFToken": getCookieName("csrftoken"),
        },
      })
      .then((response) => {
        console.log(response);
        confirm("Sign up successfully!");
      })
      .catch((error) => {
        alert(error);
      });
  }
}