import { Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField } from "@mui/material";

export const SongDetailsModal = ({ isModalOpen, selectedSong, rating, setRating, handleCloseModal, handleSubmitRating }) => (
    <Dialog open={isModalOpen} onClose={handleCloseModal}>
      <DialogTitle>Song Details</DialogTitle>
      <DialogContent>
        {selectedSong && (
          <div>
            {Object.keys(selectedSong).map((key) => (
              <p key={key}><strong>{key}:</strong> {selectedSong[key]}</p>
            ))}
            <TextField
              label="Rate the Song (1-5)"
              type="number"
              inputProps={{ min: "0", max: "5" }}
              value={rating}
              onChange={(e) => setRating(e.target.value)}
              fullWidth
              margin="dense"
            />
          </div>
        )}
      </DialogContent>
      <DialogActions>
        <Button onClick={handleCloseModal}>Cancel</Button>
        <Button onClick={handleSubmitRating} color="primary">Submit Rating</Button>
      </DialogActions>
    </Dialog>
  );
  