import { Button } from "@mui/material";

export const Pagination = ({ currentPage, prevPage, nextPage, fetchSongs }) => (
    <div className="flex justify-between mt-4">
      <Button onClick={() => fetchSongs(prevPage)} disabled={!prevPage} style={{ border: '1px solid #000' }}>Previous</Button>
      <span>Page {currentPage}</span>
      <Button onClick={() => fetchSongs(nextPage)} disabled={!nextPage} style={{ border: '1px solid #000' }}>Next</Button>
    </div>
);
  