/* ==========================================================================
   AI Governance Design Index — small enhancements
   --------------------------------------------------------------------------
   You do not need to edit this file to change any scores.

   The HTML table IS the data. This script only:
     1. recomputes each axis average from the individual scores in the table,
        so the averages can never disagree with the numbers above them;
     2. draws the little bar under each score;
     3. copies the axis averages into the summary cards at the top;
     4. highlights a column when you hover it, to help read a wide table;
     5. fills in the current year in the footer.

   If JavaScript is switched off, everything still works — the page just uses
   the averages written into the HTML instead of recalculating them.
   ========================================================================== */

(function () {
  "use strict";

  /* ---- 1 + 2. Score bars, and axis averages recomputed from the table ---- */

  function paintBars(root) {
    root.querySelectorAll("td.score[data-score]").forEach(function (cell) {
      var v = parseFloat(cell.getAttribute("data-score"));
      if (isNaN(v)) return;
      var bar = cell.querySelector(".bar");
      if (!bar) {
        bar = document.createElement("span");
        bar.className = "bar";
        cell.appendChild(bar);
      }
      bar.style.width = Math.max(0, Math.min(100, v)) + "%";
    });
  }

  function recomputeMeans(table) {
    var means = {}; // { axisKey: { frameworkKey: value } }

    table.querySelectorAll("tbody[data-axis]").forEach(function (body) {
      var axis = body.getAttribute("data-axis");
      var totals = {}, counts = {};

      body.querySelectorAll("tr:not(.mean-row)").forEach(function (row) {
        row.querySelectorAll("td.score[data-fw]").forEach(function (cell) {
          var fw = cell.getAttribute("data-fw");
          var v = parseFloat(cell.getAttribute("data-score"));
          if (isNaN(v)) return;
          totals[fw] = (totals[fw] || 0) + v;
          counts[fw] = (counts[fw] || 0) + 1;
        });
      });

      var meanRow = body.querySelector("tr.mean-row");
      means[axis] = {};

      Object.keys(totals).forEach(function (fw) {
        var mean = Math.round(totals[fw] / counts[fw]);
        means[axis][fw] = mean;
        if (!meanRow) return;
        var cell = meanRow.querySelector('td.score[data-fw="' + fw + '"]');
        if (!cell) return;
        cell.setAttribute("data-score", String(mean));
        var bar = cell.querySelector(".bar");
        cell.textContent = String(mean);
        if (bar) cell.appendChild(bar);
      });
    });

    paintBars(table);
    return means;
  }

  /* ---- 3. Summary cards at the top of the scores page -------------------- */

  function fillSummary(means) {
    document.querySelectorAll(".summary-card[data-fw]").forEach(function (card) {
      var fw = card.getAttribute("data-fw");
      card.querySelectorAll("[data-axis]").forEach(function (row) {
        var axis = row.getAttribute("data-axis");
        var value = means[axis] && means[axis][fw];
        if (value === undefined) return;
        var out = row.querySelector(".v");
        var fill = row.parentNode.querySelector('.track[data-axis="' + axis + '"] .fill');
        if (out) out.textContent = value;
        if (fill) fill.style.width = value + "%";
      });
    });
  }

  /* ---- 4. Column highlight on a wide table ------------------------------- */

  function columnHighlight(table) {
    var active = -1;

    function setColumn(index, on) {
      table.querySelectorAll("tr").forEach(function (row) {
        var cell = row.children[index];
        if (cell) cell.style.background = on
          ? "color-mix(in srgb, currentColor 6%, transparent)"
          : "";
      });
    }

    table.addEventListener("mouseover", function (event) {
      var cell = event.target.closest("td, th");
      if (!cell || !cell.parentNode.parentNode.closest("table")) return;
      var index = cell.cellIndex;
      if (index === active || index < 1) return;
      if (active > 0) setColumn(active, false);
      active = index;
      setColumn(active, true);
    });

    table.addEventListener("mouseleave", function () {
      if (active > 0) setColumn(active, false);
      active = -1;
    });
  }

  /* ---- 5. Footer year ---------------------------------------------------- */

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Run --------------------------------------------------------------- */

  var matrix = document.querySelector("table.matrix");
  if (matrix) {
    var means = recomputeMeans(matrix);
    fillSummary(means);
    if (window.matchMedia("(hover: hover)").matches) columnHighlight(matrix);
  }

  document.querySelectorAll(".summary .mini .fill").forEach(function (fill) {
    if (!fill.style.width) {
      var v = fill.getAttribute("data-score");
      if (v) fill.style.width = v + "%";
    }
  });
})();
