import axios from "axios";

const API_URL = "http://localhost:8000/api/";

export const getAllSongs = async (pageUrl = `${API_URL}songs/`) => {
  try {
    const res = await axios.get(pageUrl);
    return res.data;
  } catch (error) {
    console.error("Error fetching songs:", error);
    return { results: [], next: null, previous: null };
  }
};

export const getSongByTitle = async (songTitle) => {
  try {
    const res = await axios.get(`${API_URL}songs/${encodeURIComponent(songTitle)}/`);
    return res.data;
  } catch (error) {
    console.error("Error fetching song by title:", error);
    throw error;
  }
};

export const rateSong = async (payload) => {
  try {
    const res = await axios.post(`${API_URL}rate_song/`, payload, {
      headers: { "Content-Type": "application/json" },
    });
    return res.data;
  } catch (error) {
    console.error("Error rating song:", error.response?.data || error);
    throw error;
  }
};
