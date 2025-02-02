import { Button } from "@mui/material";

export const DownloadButton = ({ handleDownloadCSV }) => (
    <Button className="mt-4" onClick={handleDownloadCSV} style={{ border: '1px solid #000' }}>Download CSV</Button>
);
  