// static/js/admin.js

document.addEventListener("DOMContentLoaded", function () {
    const studentList = document.getElementById("studentList");

    // Placeholder dynamic content
    const sampleStudents = [
        { name: "John Doe", violations: 2 },
        { name: "Jane Smith", violations: 0 },
        { name: "Alex Johnson", violations: 1 }
    ];

    let html = "<table border='1' style='width:100%; text-align:left;'><tr><th>Student</th><th>Violations</th></tr>";

    sampleStudents.forEach(student => {
        html += <tr><td>${student.name}</td><td>${student.violations}</td></tr>;
    });

    html += "</table>";

    studentList.innerHTML = html;
});