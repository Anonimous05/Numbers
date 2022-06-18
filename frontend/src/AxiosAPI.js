import axios from "axios";

export const AxiosAPI = axios.create({
    baseURL: 'http://localhost:8000/api/v1/'
})