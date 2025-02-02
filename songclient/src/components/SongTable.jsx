import { Table } from "@mui/material";

export const SongTable = ({ songs, filteredSongs }) => (
    <Table style={{ width: "100%", borderCollapse: "collapse", marginBottom: '1rem' }}>
      <thead>
        <tr>
          {songs.length > 0 && Object.keys(songs[0]).map((key) => (
            <th 
              key={key} 
              style={{ padding: "12px", textAlign: "left", minWidth: "250px", borderBottom: "1px solid #ccc", cursor: "pointer" }}>
              {key}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredSongs.map((song, index) => (
          <tr key={index}>
            {Object.values(song).map((value, i) => (
              <td key={i} style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
  