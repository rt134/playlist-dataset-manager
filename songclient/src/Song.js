import React, { useState, useEffect } from "react";
import { saveAs } from "file-saver";
import { getAllSongs, getSongByTitle, rateSong } from "./services/songs";
import { SongSearch } from './components/SongSearch';
import { SongTable } from './components/SongTable';
import { Pagination } from './components/Pagination';
import { SongDetailsModal } from './components/SongDetailsModal';
import { DownloadButton } from './components/DownloadButton';
import './App.css';


const Song = () => {
  const [songs, setSongs] = useState([]);
  const [filteredSongs, setFilteredSongs] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [searchTitle, setSearchTitle] = useState("");
  const [nextPage, setNextPage] = useState(null);
  const [prevPage, setPrevPage] = useState(null);
  const [selectedSong, setSelectedSong] = useState(null);
  const [rating, setRating] = useState("");
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchSongs();
  }, []);

  const fetchSongs = async (url) => {
    const data = await getAllSongs(url);
    setSongs(data.results);
    setFilteredSongs(data.results);
    setNextPage(data.next);
    setPrevPage(data.previous);

    if (!url) {
      setCurrentPage(1);
    } else {
      const urlObj = new URL(url, window.location.origin);
      const pageParam = urlObj.searchParams.get("page");
      setCurrentPage(pageParam ? parseInt(pageParam, 10) : 1);
    }
    
  };

  const handleDownloadCSV = () => {
    if (songs.length === 0) return;
    
    const csvData = [
      Object.keys(songs[0]).join(","),
      ...songs.map(song => Object.values(song).join(","))
    ].join("\n");
    
    const blob = new Blob([csvData], { type: "text/csv;charset=utf-8;" });
    saveAs(blob, "songs.csv");
  };

  const handleSearch = async () => {
    if (!searchTitle.trim()) return;
    
    try {
      const song = await getSongByTitle(searchTitle);
      handleOpenModal(song);
    } catch (error) {
      console.error("Song not found.");
    }
  };

  const handleOpenModal = (song) => {
    setSelectedSong(song);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedSong(null);
    setRating("");
    setSearchTitle("")
  };

  const handleSubmitRating = async () => {
    if (!rating || !selectedSong) return;
  
    const ratingValue = parseInt(rating, 10);
    if (isNaN(ratingValue) || ratingValue < 1 || ratingValue > 5) {
      console.error("Invalid rating value. Must be between 1 and 5.");
      return;
    }

    const payload = {
      song_id: selectedSong.song_id,
      rating: ratingValue,
    };

    try {
      await rateSong(payload);
      console.log("Rating submitted successfully!");
      handleCloseModal();
    } catch (error) {
      console.error("Error submitting rating:", error);
    }
  };

  return (
    <div>
      <div className="p-4 centered-container padded-container">
        <SongSearch searchTitle={searchTitle} setSearchTitle={setSearchTitle} handleSearch={handleSearch} />
      </div>
  
      <div className="w-full max-w-md padded-container">
        <SongTable songs={songs} filteredSongs={filteredSongs} />
      </div>
  
      <div className="p-4 centered-container padded-container">
        <Pagination currentPage={currentPage} prevPage={prevPage} nextPage={nextPage} fetchSongs={fetchSongs} />
      </div>
  
      <div className="p-4 centered-container padded-container">
        <SongDetailsModal
          isModalOpen={isModalOpen}
          selectedSong={selectedSong}
          rating={rating}
          setRating={setRating}
          handleCloseModal={handleCloseModal}
          handleSubmitRating={handleSubmitRating}
        />
      </div>
  
      <div className="p-4 centered-container padded-container">
        <DownloadButton handleDownloadCSV={handleDownloadCSV} />
      </div>
    </div>
  );
};

export default Song;
