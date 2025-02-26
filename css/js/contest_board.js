document.addEventListener("DOMContentLoaded", function () {
    fetch("../../data/crawl_data/contest_info.json")
        .then(response => response.json())
        .then(data => {
            const now = Math.floor(Date.now() / 1000); // 現在のUNIXタイム
            const contestTable = document.getElementById("contestTable");

            // 未来のコンテストをフィルタリングし、開始時間でソート
            const upcomingContests = data
                .filter(contest => contest.start_epoch_second > now) // 未来のコンテストのみ
                .sort((a, b) => a.start_epoch_second - b.start_epoch_second) // 開始時間で昇順ソート
                .slice(0, 10); // 最大10件まで表示

            // 表にデータを挿入
            upcomingContests.forEach(contest => {
                const row = document.createElement("tr");

                const date = new Date(contest.start_epoch_second * 1000);
                const formattedDate = date.toLocaleString("ja-JP", { year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" });

                const duration = Math.floor(contest.duration_second / 60) + " 分";

                row.innerHTML = `
                    <td>${formattedDate}</td>
                    <td>${duration}</td>
                    <td>${contest.title}</td>
                    <td>${contest.rate_change}</td>
                `;

                contestTable.appendChild(row);
            });

        })
        .catch(error => console.error("JSONの読み込みに失敗しました:", error));
});
