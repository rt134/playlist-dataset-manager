import { Button, Input } from "@mui/material";

export const SongSearch = ({ searchTitle, setSearchTitle, handleSearch }) => (
    <div className="flex justify-center items-center gap-4 mb-6">
      <Input value={searchTitle} onChange={(e) => setSearchTitle(e.target.value)} placeholder="Enter song title" />
      <Button onClick={handleSearch} style={{ border: '1px solid #000' }}>Get Song</Button>
    </div>
);
  